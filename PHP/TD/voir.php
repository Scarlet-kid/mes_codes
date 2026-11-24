

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Voir</title>
</head>
<body>
    <ul>
        <?php
            require ('db.php');
            $stmt = $bdd->query("SELECT livre.id,livre.titre,auteur.nom FROM livre JOIN auteur ON livre.id = auteur.id");
            $livres = $stmt->fetchAll();
            foreach ($livres as $livre) {?>
                <ul>
                    <li value="<?= $livre['id'] ?>"><?= htmlspecialchars($livre['titre']) ?> de <?= htmlspecialchars($livre['nom']) ?></li>
                </ul>
        <?php } ?>
    </ul>

    <br>
    <a href="index.php">Retour à l'accueil</a>
</body>
</html>