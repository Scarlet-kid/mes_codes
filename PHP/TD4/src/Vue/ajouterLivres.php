<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Ajouter un livre</title>
</head>
<body>
    <h1>Ajouter un livre</h1>
    <?php if (!empty($erreur)): ?>
        <p style="color:red;"><?= htmlspecialchars($erreur) ?></p>
    <?php endif; ?>

    <form action="index.php?action=traiter_ajout" method="POST">
        <label for="titre">Titre :</label>
        <input type="text" id="titre" name="titre" required><br><br>

        <label for="annee">Année :</label>
        <input type="number" id="annee" name="annee"><br><br>

        <label for="auteur_id">ID Auteur :</label>
        <input type="number" id="auteur_id" name="auteur_id" required><br><br>

        <button type="submit">Enregistrer</button>
    </form>
    <br>
    <a href="index.php">Retour à la liste</a>
</body>
</html>