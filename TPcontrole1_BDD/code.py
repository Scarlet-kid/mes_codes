import psycopg
def connect():
    return psycopg.connect(
        host = "localhost",
        dbname = "postgres",
        user = "postgres",
        password = "66793270"
    )
    
def nb_observations(conn, lb, ub):
    sql = """ SELECT Operation.idOperation, count(Observation.description) AS nb_Observations
              FROM Operation LEFT JOIN Effectue USING (idOperation)
                LEFT JOIN Observation USING (idEmploye,idOperation)
            WHERE Operation.nomProduit = 'lait' and  Operation.date >= %s  AND Operation.date< %s
            GROUP BY idOperation
        """

    with conn.execute(sql,[lb, ub]) as cur:
        res = cur.fetchall()
    return res

def nomEmpty(conn, sql):
    with conn.execute(sql) as cur:
        return cur.fetchone() is None

def verifier_list_employe(conn,le):
    sql = """SELECT Employe.idEmploye FROM Employe;"""
    
    with conn.execute(sql) as cur:
        if not le:
            return True
        
        if not nomEmpty(conn, sql):
            all = True
            res = cur.fetchall()
            print(res[0])
            for i in le:
                if i not in res:
                    all = False
            return all
        return True
    
def produit_nature(conn,lb,ub,n1,n2):
    sql = """ SELECT Operation.nomProduit
    FROM Operation
    WHERE Operation.nature = %s AND Operation.date  >= %s  AND Operation.date< %s
    INTERSECT
    SELECT Operation.nomProduit
    FROM Operation
    WHERE Operation.nature = %s AND Operation.date  >= %s  AND Operation.date< %s """

    with conn.execute(sql,[n1,lb,ub,n2,lb,ub]) as cur:
        return [row[0] for row in cur.fetchall()]
        
def prog():
    conn = connect()
    #print(nb_observations(conn,'01-03-2026','29-03-2026'))
    #print(verifier_list_employe(conn,[1]))
    print(produit_nature(conn,'01-03-2026','29-03-2026','rangement','Commande'))

if __name__ == "__main__":
    prog()