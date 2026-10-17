<?php
$host = 'localhost';
$port = '5432'; // Port par défaut de PostgreSQL
$dbname = 'postgres';
$user = 'postgres';
$password = '66793270';

try {
    // Connexion PostgreSQL via PDO
    $bdd = new PDO("pgsql:host=$host;port=$port;dbname=$dbname", $user, $password);
    $bdd->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Erreur de connexion : " . $e->getMessage());
}
?>