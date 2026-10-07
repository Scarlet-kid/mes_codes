<?php
namespace App\Modele;  

use PDO;

class LivreRepository {
    private PDO $pdo;

    public function __construct(PDO $pdo) {
        $this->pdo = $pdo;
    }

    
    public function findAll(): array {
        $sql = "SELECT l.id, l.titre, l.annee, l.auteur_id, a.nom AS auteur_nom 
                FROM livres l 
                JOIN auteurs a ON l.auteur_id = a.id 
                ORDER BY l.id DESC"; // la requete
        $stmt = $this->pdo->query($sql); // je pense le .query pour tout ce qui requette de select : simplifiable la requete.
        $results = $stmt->fetchAll();

        $livres = [];
        foreach ($results as $row) {
            $livres[] = new Livre(
                $row['titre'],
                (int)$row['auteur_id'],
                $row['annee'] ? (int)$row['annee'] : null,
                (int)$row['id'],
                $row['auteur_nom']
            );
        }
        return $livres;
    }

    
    public function create(Livre $livre): bool {
        $sql = "INSERT INTO livres (titre, annee, auteur_id) VALUES (:titre, :annee, :auteur_id)";
        $stmt = $this->pdo->prepare($sql);
        return $stmt->execute([
            ':titre' => $livre->getTitre(),
            ':annee' => $livre->getAnnee(),
            ':auteur_id' => $livre->getAuteurId()
        ]);
    }
}