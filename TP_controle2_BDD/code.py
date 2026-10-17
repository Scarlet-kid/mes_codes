import psycopg

def connect():
    return psycopg.connect(
        host = "localhost",
        dbname = "postgres",
        user = "postgres",
        password = "66793270"
    )
    
def guide_nb_perso(conn, id_guilde):
    sql = """ SELECT nb_membres FROM vue_membres_guilde WHERE nom_guilde = %s; """
    
    # On ouvre le curseur
    with conn.execute(sql, [id_guilde]) as cur:
        row = cur.fetchone()
        if row is not None:
            return row[0]  # On renvoie juste le chiffre (ex: 5)
        return 0  # Si la guilde n'existe pas
  
    
def guilde_max_nb_membres(conn):
    sql = """ WITH guilde_max_membres AS(
    SELECT max(nb_de_membres) AS val_max
    FROM PersoParGuilde
    ) SELECT PersoParGuilde.nom, guilde_max_membres.val_max
FROM PersoParGuilde,guilde_max_membres WHERE PersoParGuilde.nb_de_membres = guilde_max_membres.val_max;"""
    with conn.execute(sql) as cur:
        return cur.fetchall()
    
def perso_quete(conn):
    sql = """ SELECT Personnage.idPersonnage
    FROM Personnage
    EXCEPT
    SELECT DISTINCT Participe.idPersonnage
    FROM Participe; """
    with conn.execute(sql) as cur:
        return cur.fetchall()
        
def perso_sans_guilde(conn):
    sql = """ SELECT Personnage.nom, PersoGuilde.nom
FROM Personnage LEFT JOIN PersoGuilde USING (idPersonnage)
WHERE PersoGuilde.nom IS NULL ; """
    with conn.execute(sql) as cur:
        return cur.fetchall()
    
def prog():
    conn = connect()
    #print(conn, 'Fairy Tail')
    #print(guilde_max_nb_membres(conn))
    #print(perso_quete(conn))
    print(perso_sans_guilde(conn))

if __name__ == '__main__':
    prog()