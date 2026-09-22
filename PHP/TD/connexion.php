<?php
session_start(); // Toujours en première ligne

// Simulation d'un utilisateur inscrit en base de données
$utilisateur_bdd = "admin";
// "secret123" haché avec l'algorithme sécurisé de PHP
$hash_bdd = password_hash("secret123", PASSWORD_DEFAULT);

$erreur = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $login = trim($_POST['login'] ?? '');
    $mdp = $_POST['mdp'] ?? '';

    // Vérification du login et du mot de passe haché
    if ($login === $utilisateur_bdd && password_verify($mdp, $hash_bdd)) {
        // Authentification réussie : enregistrement de la session
        $_SESSION['utilisateur'] = $login;
        
        // Redirection vers la page membre
        header("Location: membre.php");
        exit();
    } else {
        $erreur = "Identifiants incorrects.";
    }
}
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Connexion</title>
</head>
<body>

    <h1>Connexion</h1>

    <?php if ($erreur): ?>
        <p style="color: red;"><?= htmlspecialchars($erreur) ?></p>
    <?php endif; ?>

    <form method="POST">
        <div>
            <label for="login">Identifiant :</label>
            <input type="text" id="login" name="login" required>
        </div>
        <br>
        <div>
            <label for="mdp">Mot de passe :</label>
            <input type="password" id="mdp" name="mdp" required>
        </div>
        <br>
        <button type="submit">Se connecter</button>
    </form>

</body>
</html>