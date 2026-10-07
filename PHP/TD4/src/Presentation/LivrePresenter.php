<?php
namespace App\Presentation;

use App\Modele\LivreRepository;
use App\Modele\Livre;

class LivrePresenter {
    private LivreRepository $repository;

    public function __construct(LivreRepository $repository) {
        $this->repository = $repository;
    }

    public function afficherListe(): void {
        $livres = $this->repository->findAll();
        require __DIR__ . '/../Vue/listeLivres.php'; 
    }

    public function traiterAjout(array $postData): void {
        $titre = trim($postData['titre'] ?? '');
        $annee = !empty($postData['annee']) ? (int)$postData['annee'] : null;
        $auteurId = !empty($postData['auteur_id']) ? (int)$postData['auteur_id'] : 0;

        if (!empty($titre) && $auteurId > 0) {
            $nouveauLivre = new Livre($titre, $auteurId, $annee);
            $this->repository->create($nouveauLivre);
            header('Location: index.php');
            exit();
        }
        
        $erreur = "Veuillez remplir tous les champs obligatoires.";
        require __DIR__ . '/../Vue/ajouterLivres.php';
    }
}