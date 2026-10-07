<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Médiathèque - Liste des livres</title>
</head>
<body>
    <h1>Liste des livres</h1>
    <a href="index.php?action=ajouter">Ajouter un livre</a>
    <ul>
        <?php foreach ($livres as $livre): ?>
            <li>
                <strong><?= htmlspecialchars($livre->getTitre()) ?></strong> 
                (<?= $livre->getAnnee() ?? 'N/A' ?>) — 
                Auteur : <?= htmlspecialchars($livre->getAuteurNom()) ?>
            </li>
        <?php endforeach; ?>
    </ul>
</body>
</html>