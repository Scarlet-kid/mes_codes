import psycopg
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# --- CONFIGURATION ---
# Database connection parameters

def connect():
    return psycopg.connect(
        host = "localhost",
        dbname = "postgres",
        user = "postgres",
        password = "66793270"
    )

def generate_control_chart(conn,sensor_id):

    sql_mean_stddev =""" SELECT
    AVG(c.controlValue - s.sensorValue) AS mean_error,
    STDDEV(c.controlValue - s.sensorValue) AS stddev_error
    FROM ControlMeasurement c
    JOIN SensorMeasurement s ON c.sensorId = s.sensorId
    AND c.sensorTimestamp = s.timestamp
    WHERE c.sensorId = %s;
    """

    with conn.execute(sql_mean_stddev,[sensor_id]) as cur:
        stats = cur.fetchone()
    if stats[0] is None:
        print(f"No data found for Sensor ID {sensor_id}.")
        return

    mu = float(stats[0])
    sigma = float(stats[1])

    data_query = """
                    WITH LastControlDate AS (
                        SELECT MAX(controlTimestamp) AS max_date
                        FROM ControlMeasurement
                        WHERE sensorId = %s
                    )
                    SELECT
                        c.controlTimestamp,
                        (c.controlValue - s.sensorValue) AS error_value
                    FROM ControlMeasurement c
                    JOIN SensorMeasurement s
                      ON c.sensorId = s.sensorId
                     AND c.sensorTimestamp = s.timestamp
                    CROSS JOIN LastControlDate lcd
                    WHERE c.sensorId = %s
                      AND c.controlTimestamp >= (lcd.max_date - INTERVAL '8 days')
                    ORDER BY c.controlTimestamp ASC;
                """
    with conn.execute(data_query, (sensor_id, sensor_id)) as cur:
        records = cur.fetchall()

    if not records:
        print(f"No control measurements found in the last 8 days for Sensor {sensor_id}.")
        return

    # Separate dates and error values for matplotlib
    timestamps = [row[0] for row in records]
    errors = [float(row[1]) for row in records]

    # ---------------------------------------------------------
    # 3. Plot the Control Chart
    # ---------------------------------------------------------
    plt.figure(figsize=(12, 6))

    # Plot the error points
    plt.plot(timestamps, errors, marker='o', linestyle='-', color='steelblue', label='Measurement Error')

    # Plot Mean (mu)
    plt.axhline(y=mu, color='black', linestyle='-', linewidth=2, label=f'Mean (mu): {mu:.4f}')

    # Plot Upper and Lower Control Limits (mu + 2*sigma, mu - 2*sigma)
    ucl = mu + 2 * sigma
    lcl = mu - 2 * sigma
    plt.axhline(y=ucl, color='red', linestyle='--', linewidth=1.5, label=f'UCL (mu + 2 sigma): {ucl:.4f}')
    plt.axhline(y=lcl, color='red', linestyle='--', linewidth=1.5, label=f'LCL (mu - 2 sigma): {lcl:.4f}')

    # Formatting the chart
    plt.title(f'Control Chart for Sensor ID {sensor_id} (Last 8 Days)')
    plt.xlabel('Time')
    plt.ylabel('Error Value (Manual - Automatic)')
    plt.grid(True, alpha=0.3)
    plt.legend(loc='best')

    # Format the x-axis dates nicely
    plt.gca().xaxis.set_major_formatter(DateFormatter('%Y-%m-%d %H:%M'))
    plt.xticks(rotation=45)
    plt.tight_layout() # Adjusts layout so dates don't get cut off

    # Show the plot
    plt.show()

    print(f"Global Statistics for Sensor {sensor_id}:")
    print(f"- Mean (mu): {mu:.4f}")
    print(f"- Standard Deviation (sigma): {sigma:.4f}")
    print(f"- Number of points plotted (last 8 days): {len(timestamps)}")

# Run the function
conn = connect()
generate_control_chart(conn,1)