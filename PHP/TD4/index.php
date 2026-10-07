<?php
// Chargement manuel des classes (Autoload simplifié)
require_once __DIR__ . '/config/Database.php';
require_once __DIR__ . '/src/Modele/Livre.php';
require_once __DIR__ . '/src/Modele/LivreRepository.php';
require_once __DIR__ . '/src/Presentation/LivrePresenter.php';

use Config\Database;
use App\Modele\LivreRepository;
use App\Presentation\LivrePresenter;

// Initialisation des dépendances
$db = (new Database())->getConnection();
$repository = new LivreRepository($db);
$presenter = new LivrePresenter($repository);

// Routage simple par paramètre URL (?action=...)
$action = $_GET['action'] ?? 'liste';

switch ($action) {
    case 'ajouter':
        require __DIR__ . '/src/Vue/ajouterLivres.php';
        break;
    case 'traiter_ajout':
        $presenter->traiterAjout($_POST);
        break;
    case 'liste':
    default:
        $presenter->afficherListe();
        break;
}