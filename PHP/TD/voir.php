<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Voir</title>
</head>
<body>
    <?php
        $livres = [['titre'=>'Dune','auteur' => 'Frank Herbert' ], [ 'titre' => '1984', 'auteur' => 'George Orwell' ],
                  ['titre' => 'Le Petit Prince', 'auteur' => 'Antoine de Saint-Exupéry' ]];

    ?>

    <ul>
        <?php foreach ($livres as $livre): ?>
            <li>
                <strong><?= ' '.($livre['titre']) ?></strong> 
                de <?= ' '.($livre['auteur']) ?>
            </li>
        <?php endforeach; ?>
    </ul>

    <br>
    <a href="index.php">Retour à l'accueil</a>
</body>
</html>