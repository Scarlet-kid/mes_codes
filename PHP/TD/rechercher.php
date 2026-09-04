<?php
// Données de démonstration
$livres = [
    ['titre' => 'Dune', 'auteur' => 'Frank Herbert', 'categorie' => 'Science-Fiction'],
    ['titre' => '1984', 'auteur' => 'George Orwell', 'categorie' => 'Science-Fiction'],
    ['titre' => 'Le Petit Prince', 'auteur' => 'Antoine de Saint-Exupéry', 'categorie' => 'Roman'],
    ['titre' => 'Astérix le Gaulois', 'auteur' => 'René Goscinny', 'categorie' => 'BD']
];

// Récupération de la recherche transmise via la méthode GET
$recherche = trim($_GET['q'] ?? '');

// Filtrage des résultats
$resultats = [];
if (!empty($recherche)) {
    foreach ($livres as $livre) {
        // Recherche insensible à la casse dans le titre ou l'auteur
        if (stripos($livre['titre'], $recherche) !== false || stripos($livre['auteur'], $recherche) !== false) {
            $resultats[] = $livre;
        }
    }
} else {
    // Si la recherche est vide, on affiche tous les livres
    $resultats = $livres;
}
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Rechercher un livre</title>
</head>
<body>

    <h1>Recherche dans la médiathèque</h1>

    <!-- Formulaire de recherche avec la méthode GET -->
    <form action="" method="GET">
        <label for="q">Titre ou auteur :</label>
        <input type="text" id="q" name="q" value="<?= htmlspecialchars($recherche) ?>" placeholder="Ex: Dune, Orwell...">
        <button type="submit">Rechercher</button>
        <?php if (!empty($recherche)): ?>
            <a href="rechercher.php">Réinitialiser</a>
        <?php endif; ?>
    </form>

    <h2>Résultats</h2>

    <?php if (!empty($resultats)): ?>
        <ul>
            <?php foreach ($resultats as $livre): ?>
                <li>
                    <strong><?= htmlspecialchars($livre['titre']) ?></strong> 
                    de <?= htmlspecialchars($livre['auteur']) ?> 
                    <em>(<?= htmlspecialchars($livre['categorie']) ?>)</em>
                </li>
            <?php endforeach; ?>
        </ul>
    <?php else: ?>
        <p>Aucun livre ne correspond à votre recherche "<strong><?= htmlspecialchars($recherche) ?></strong>".</p>
    <?php endif; ?>

    <br>
    <a href="index.php">Retour à l'accueil</a>

</body>
</html>