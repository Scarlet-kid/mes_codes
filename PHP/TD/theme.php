<?php
// On récupère le thème actuel depuis le cookie, 'light' par défaut
$theme = $_COOKIE['theme'] ?? 'light';

// Si l'utilisateur clique sur le bouton pour changer de thème
if (isset($_POST['changer_theme'])) {
    $theme = ($_POST['changer_theme'] === 'dark') ? 'dark' : 'light'; // un if/else
    
    // On enregistre le cookie pour 30 jours
    setcookie("theme", $theme, time() + (30 * 24 * 60 * 60));
    
    // Recharge la page pour appliquer immédiatement le cookie
    header("Location: theme.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Choix du thème</title>
    <style>
        body.light { background-color: #ffffff; color: #000000; } 
        body.dark { background-color: #121212; color: #ffffff; }
    </style>
</head>
<body class="<?= htmlspecialchars($theme) ?>"> <!--une autre facon de faire un echo-->

    <h1>Préférence de thème</h1>
    <p>Thème actuel : <strong><?= htmlspecialchars($theme) ?></strong></p>

    <form method="POST">
        <?php if ($theme === 'light'): ?>
            <button type="submit" name="changer_theme" value="dark">Passer au thème sombre</button>
        <?php else: ?>
            <button type="submit" name="changer_theme" value="light">Passer au thème clair</button>
        <?php endif; ?>
    </form>

</body>
</html>