<?php
session_start();

// Contrôle d'accès : si la variable de session n'existe pas,
if (!isset($_SESSION['utilisateur'])) {
    header("Location: connexion.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Espace Membre</title>
</head>
<body>

    <h1>Espace réservé</h1>
    <p>Bienvenue **<?= htmlspecialchars($_SESSION['utilisateur']) ?>** ! Vous êtes connecté.</p>

    <p><a href="deconnexion.php">Se déconnecter</a></p>

</body>
</html>