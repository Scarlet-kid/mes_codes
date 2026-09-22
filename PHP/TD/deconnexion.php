<?php
session_start();

// 1. Libère toutes les variables de session
session_unset();

// 2. Détruit la session sur le serveur
session_destroy();

// 3. Redirige vers la page de connexion
header("Location: connexion.php");
exit();
?>