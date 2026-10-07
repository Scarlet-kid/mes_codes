DROP TABLE IF EXISTS Ville, Trajet, Reduction, Billet, Tarif CASCADE ;

CREATE TABLE Ville
(
    ville TEXT PRIMARY KEY
);

CREATE TABLE Trajet
(
    idTrajet INT PRIMARY KEY ,
    depart TEXT REFERENCES Ville(ville),
    arrivee TEXT REFERENCES ville(ville),
    dateDepart timestamp,
    nbVoiture INT NOT NULL
);

CREATE TABLE Reduction
(
    nomReduction TEXT PRIMARY KEY
);

CREATE TABLE Tarif
(
    idTrajet INT REFERENCES Trajet(idTrajet),
    nomReduction TEXT REFERENCES Reduction(nomReduction),
    PRIMARY KEY (idTrajet,nomReduction),
    tarif INT
);

CREATE TABLE Billet
(
    noBillet INT PRIMARY KEY ,
    idTrajet INT,
    nomReduction TEXT,
    FOREIGN KEY (idTrajet,nomReduction) REFERENCES Tarif(idTrajet, nomReduction),
    voiture INT NOT NULL ,
    siege INT NOT NULL
);

INSERT INTO Ville VALUES
                         ('Lille'),
                         ('Paris'),
                         ('Valenciennes');

INSERT INTO Trajet VALUES (000,'Lille','Valenciennes','28-01-2012',10),
                          (005,'Lille','Paris','28-01-2012',10),
                          (006,'Lille','Valenciennes','28-01-2012',10),
                          (007,'Lille','Valenciennes','28-01-2012',10),




                            (001,'Valenciennes','Paris','28-01-2012',10),
                            (002,'Valenciennes','Paris','28-01-2012',10),
                          (004,'Valenciennes','Paris','28-01-2012',10),
                          (003,'Valenciennes','Paris','27-01-2012',10);

INSERT INTO Reduction VALUES ('Carte Liberte'),
                             ('Carte Avantage Jeune'),
                             ('Carte 12-25'),
                             ('TGV Prems 2eme classe'),
                             ('Normal');

INSERT INTO Tarif VALUES (001,'Carte Liberte',100),
                         (002,'Carte Liberte',50),
                         (002,'Carte Avantage Jeune',40),
                         (001,'TGV Prems 2eme classe',40),
                         (004,'Carte Avantage Jeune',70),
                         (002,'TGV Prems 2eme classe',80),

                         (000,'Normal',8.80),
                         (000,'Carte 12-25',6.60);


INSERT INTO Billet VALUES (1000,001,'Carte Liberte',5,14),
                          (2000,001,'TGV Prems 2eme classe',6,10),
                          (3000,002,'Carte Avantage Jeune',15,8);


SELECT Trajet.*,Tarif.nomReduction
FROM Trajet JOIN Tarif USING (idTrajet)
WHERE Trajet.depart = 'Valenciennes' and Trajet.dateDepart='28-01-2012' and Tarif.nomReduction != 'TGV Prems 2eme classe';

SELECT Trajet.arrivee
FROM Trajet
WHERE Trajet.depart='Lille' and Trajet.dateDepart = '28-01-2012'
GROUP BY Trajet.depart, Trajet.arrivee;



