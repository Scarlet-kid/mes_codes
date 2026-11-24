<?php
$categories = ['BD', 'Science-Fiction', 'Roman', 'Manga', 'Essai'];

$titre = '';
$auteur = '';
$categorie_selectionnee = '';
$message_succes = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Récupération des données
    $titre = trim($_POST['titre'] ?? ''); // trim pour effacer les espace en début et fin de caractère.
    $auteur = trim($_POST['auteur'] ?? '');
    $categorie_selectionnee = $_POST['categorie'] ?? '';

    // Traitement si tout est valide
    $message_succes = "Le livre <strong>" . htmlspecialchars($titre) . "</strong> (" . htmlspecialchars($categorie_selectionnee) . ") de <strong>" . htmlspecialchars($auteur) . "</strong> a été ajouté avec succès !";
    // Réinitialisation des champs
    $titre = '';
    $auteur = '';
    $categorie_selectionnee = '';

}
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Ajouter un livre</title>
</head>
<body>

    <h1>Ajouter un livre à la médiathèque</h1>

    <!-- Affichage du message de succès -->
    <?php if (!empty($message_succes)): ?>
        <p style="color: green;"><?= $message_succes ?></p>
    <?php endif; ?>

    <!-- Formulaire -->
    <form action="" method="POST">
        <div>
            <label for="titre">Titre :</label>
            <input type="text" id="titre" name="titre" value="<?= htmlspecialchars($titre)?>" <?= htmlspecialchars($titre) ?>>
            <!-- La valeur du value c'est ce qui sera transmis lors POST -->
        </div>
        <br>
        <div>
            <label for="auteur">Auteur :</label>
            <input type="text" id="auteur" name="auteur" value="<?= htmlspecialchars($auteur) ?>">
        </div>
        <br>
        <div>
            <label for="categorie">Catégorie :</label>
            <select id="categorie" name="categorie">
                <option value="">-- Choisir une catégorie --</option>
                <?php foreach ($categories as $cat): ?>
                    <option value="<?= htmlspecialchars($cat) ?>"> <?= htmlspecialchars($cat) ?>
                    </option>
                <?php endforeach; ?>
            </select>
        </div>
        <br>
        <button type="submit">Ajouter le livre</button>
    </form>
    <br>
    <a href="index.php">Retour à l'accueil</a>
</body>
</html>