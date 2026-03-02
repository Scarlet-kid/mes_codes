import psycopg
def connect():
    return psycopg.connect(
        host = "iutinfo-sgbd.uphf.fr",
        dbname = "capteurs",
        user = "iutinfo573",
        password = "idhaGxeW"
    )

class Sensor:
    def __init__(self,sensorId,validity,position):
        self.id = sensorId
        self.validity = validity
        self.position = position
    def __str__(self):
        return f"id = {self.id}, validité = {self.validity}, Position = {self.position}"

def renvoieSensor(conn, idSensor):
    sql = """ SELECT sensorId, validity , position FROM Sensor WHERE sensorId = %s"""
    with conn.execute(sql,[idSensor]) as cur:
        sensor = cur.fetchone()
        if sensor is not None:
            return Sensor(sensor[0],sensor[1],sensor[2])

def renvoieAllSensor(conn):
    sql = """
        SELECT sensor.sensorid, sensor.validity, sensor.position
        FROM sensor JOIN model USING (modelid)
        WHERE model.unit='psi'
        """
    with conn.execute(sql) as cur:
        sensor = cur.fetchone()
        if sensor is not None:
            return Sensor(sensor[0],sensor[1],sensor[2])

def renvoieAllSensor2(conn,unit):
    sql = """
        SELECT sensor.sensorid, sensor.validity, sensor.position
        FROM sensor JOIN model USING (modelid)
        WHERE model.unit = %s
        """
    with conn.execute(sql,[unit]) as cur:
        sensor = cur.fetchone()
        if sensor is not None:
            return Sensor(sensor[0],sensor[1],sensor[2])
        
def connect2():
    return psycopg.connect(
        host = "iutinfo-sgbd.uphf.fr",
        dbname = "iutinfo573",
        user = "iutinfo573",
        password = "idhaGxeW"
    )
from datetime import datetime

def EnregistrerMesure(conn,idSensor,valeur):
    sql = """
    INSERT INTO sensormesurement (sensorId,date,sensorValue) VALUES (%s, %s, %s)
    """
    date = datetime.now()
    conn.execute(sql,[idSensor,date,valeur])
    conn.commit()
    return date


if __name__ == "__main__":
    conn = connect()
    #print(renvoieSensor(conn,1))
    #print(renvoieAllSensor(conn))
    #print(renvoieAllSensor2(conn,'°C'))
    conn2 = connect2()
    print(EnregistrerMesure(conn2,2,555))


