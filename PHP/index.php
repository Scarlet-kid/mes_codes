<?php
    require 'connexion.php';
    $sql = 'SELECT titre,nom FROM livre JOIN auteur on livre.auteur_id=auteur.id ORDER BY titre';
    $stmt = $pdo->query($sql);
    $livres = $stmt->fetchall(PDO::FETCH_ASSOC);
?>

<!doctype html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Médiathèque</title>
</head>
<body>
    <h1>Bienvenue</h1>
    <p>Bienvenue dans notre médiathèque</p>
    <ul>
        <li><a href="ajout.html">Ajouter des livres</a></li>
        <li><a href="voir.php">Voir les livres</a></li>
        <li><a href="recherche.php">Rechercher des livres</a></li>
    </ul>
    <h2 id="listes">La liste des livres</h2>
    <ul>
        <?php foreach ($livres as $livre):?>
            <li> <?=htmlspecialchars($livre['titre'])?> - <?=htmlspecialchars($livre['auteur'])?></li>
        <?php endforeach; ?>
    </ul>
    
    
</body>
</html>