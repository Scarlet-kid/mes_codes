<?php
    require 'connexion.php';
    if ($_SERVER['REQUEST_METHOD'] === 'POST')
    {
        $titre = $_POST['titre'] ?? '';
        $annee = $_POST['annee'] ?? null;
        $auteur_id = $_POST['auteur'];
        if($titre === ''){$error = 'le titre est obligatoire';}
        else{
            $sql = 'INSERT INTO livre(titre,annee,auteur_id) VALUES (:title,:years,:author_id)';
            $stmt = $pdo->preapare($sql);
            $stmt->execute(['title'=>$titre, 'years'=>$annee, 'author_id'=>$auteur_id]);
            header('Location:index.php');
            exit();
        }

    }
?>

<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Formulaire d'ajout</title>
</head>
<body>
    <form action="" method="post">
        <H1>Ajouter un livre</H1>
        <p>
            <label for="titre">Titre : </label>
            <input type="text" id="titre" name="titre">
        </p>
        
        <p>
            <label for="auteur">Auteur : </label>
            <input type="text" id="auteur" name="auteur">
        </p>

        <p>
            <label for="categorie"></label>
            <select name="categorie" id="categorie">
            <option value="">--choisir---</option>
            <?php
                require 'connexion.php';
                $stmt = $pdo->query('SELECT id, nom FROM auteur ORDER BY nom');
                $authors = $stmt->fetchAll(PDO::FETCH_ASSOC);
                foreach ($authors as $author): ?>
                    <option value="<?= $author['id']?>"><?=htmlspecialchars($author['nom'])?></option>
                <?php endforeach;?>
            </select>
        </p>
        
        <p>
            <label for="annee">Année de publication</label>
            <input type="text" id="annee" name="name">
        </p>
        
        <p>
            <button type="submit">Ajouter le livre</button>
        </p>
    </form>
</body>
</html>