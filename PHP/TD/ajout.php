<?php
$categories = ['BD', 'Science-Fiction', 'Roman', 'Manga', 'Essai'];

$titre = '';
$auteur = '';
$categorie_selectionnee = '';
$message_succes = '';
$erreurs = [];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Récupération des données
    $titre = trim($_POST['titre'] ?? ''); // trim pour effacer les espace en début et fin de caractère.
    $auteur = trim($_POST['auteur'] ?? '');
    $categorie_selectionnee = $_POST['categorie'] ?? '';

    // Validation du titre
    if (empty($titre)) {
        $erreurs[] = "Le champ 'Titre' est obligatoire.";
    } elseif (strlen($titre) < 2) {
        $erreurs[] = "Le titre doit contenir au moins 2 caractères.";
    }

    // Validation de l'auteur
    if (empty($auteur)) {
        $erreurs[] = "Le champ 'Auteur' est obligatoire.";
    } elseif (strlen($auteur) < 2) {
        $erreurs[] = "Le nom de l'auteur doit contenir au moins 2 caractères.";
    }

    // Validation de la catégorie
    if (empty($categorie_selectionnee)) {
        $erreurs[] = "Veuillez sélectionner une catégorie.";
    } elseif (!in_array($categorie_selectionnee, $categories)) {
        $erreurs[] = "La catégorie sélectionnée est invalide.";
    } // optionnel le deuxieme elseif

    // Traitement si tout est valide
    if (empty($erreurs)) {
        $message_succes = "Le livre <strong>" . htmlspecialchars($titre) . "</strong> (" . htmlspecialchars($categorie_selectionnee) . ") de <strong>" . htmlspecialchars($auteur) . "</strong> a été ajouté avec succès !";
        // Réinitialisation des champs
        $titre = '';
        $auteur = '';
        $categorie_selectionnee = '';
    }
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

    <!-- Affichage des erreurs -->
    <?php if (!empty($erreurs)): ?>
        <div style="color: red;">
            <ul>
                <?php foreach ($erreurs as $erreur): ?>     <!-- Un tableau pour gerer les erreurs car il peut y avoir plusieurs erreurs -->
                    <li><?= htmlspecialchars($erreur) ?></li>
                <?php endforeach; ?>
            </ul>
        </div>
    <?php endif; ?>

    <!-- Affichage du message de succès -->
    <?php if (!empty($message_succes)): ?>
        <p style="color: green;"><?= $message_succes ?></p>
    <?php endif; ?>

    <!-- Formulaire -->
    <form action="" method="POST">
        <div>
            <label for="titre">Titre :</label>
            <input type="text" id="titre" name="titre" value="<?= htmlspecialchars($titre) ?>">
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
                    <option value="<?= htmlspecialchars($cat) ?>" <?= ($categorie_selectionnee === $cat) ? 'selected' : '' ?>>
                        <?= htmlspecialchars($cat) ?>
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