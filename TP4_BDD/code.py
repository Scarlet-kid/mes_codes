import psycopg
def connect():
    return psycopg.connect(
        host = "iutinfo-sgbd.uphf.fr",
        dbname = "iutinfo573",
        user = "iutinfo573",
        password = "idhaGxeW"
    )

def Q1(conn):
    sql = """
    SELECT Trajet.*,Tarif.nomReduction
    FROM Trajet JOIN Tarif USING (idTrajet)
    WHERE Trajet.depart = 'Valenciennes' and Trajet.dateDepart='28-01-2012' and Tarif.nomReduction != 'TGV Prems 2eme classe';
            """
    with conn.execute(sql) as cur:
        res = cur.fetchall()
    return res

def Q2(conn):
    sql = """ 
        SELECT Trajet.arrivee
        FROM Trajet
        WHERE Trajet.depart='Lille' and Trajet.dateDepart = '28-01-2012'
        GROUP BY Trajet.depart, Trajet.arrivee;
        """
    with conn.execute(sql) as cur:
        res = cur.fetchall()
    return res


def prog():
    conn = connect()
    #print(Q1(conn))
    print(Q2(conn))

if __name__ == "__main__":
    prog()