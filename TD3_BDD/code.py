
import matplotlib
from datetime import datetime

import psycopg
def connect():
    return psycopg.connect(
    host = "iutinfo-sgbd",
    dbname = "capteurs",
    user = "iutinfo134",
    password = "NuVRPnlV"
    )

class Sensor:
    def __init__(self, sensorId, position, validity):
        self.sensorId = sensorId
        self.position = position
        self.validity = validity

    def __str__(self):
        return f"Sensor {self.sensorId}: {self.position}, {self.validity}"

def loadSensor(conn, sensorId):
    sql = """SELECT sensorId, position, validity FROM Sensor WHERE sensorId =␣↪%s"""
    with conn.execute(sql, [sensorId]) as cur:
        sensor = cur.fetchone()
        if sensor is not None:
            return Sensor(sensor[0], sensor[1], sensor[2])
        
def searchUnit(conn, unit):
    sql = """SELECT sensorId, position, validity
            FROM Sensor JOIN Model USING (modelId)
            WHERE unit = %s"""
    with conn.execute(sql, [unit]) as cur:
        return [Sensor(sensor[0], sensor[1], sensor[2]) for sensor in cur]
    
with connect() as conn:
    sensor = loadSensor(conn, 1)
    print(sensor)
    sensors = searchUnit(conn, "psi")
    print([str(s) for s in sensors])


