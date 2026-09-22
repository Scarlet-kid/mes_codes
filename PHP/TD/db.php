<?php
$host = 'iutinfo-sgbd.uphf.fr';
$port = '5432'; // Port par défaut de PostgreSQL
$dbname = 'postgres';
$user = 'iutinfo573';
$password = 'idhaGxeW';

try {
    // Connexion PostgreSQL via PDO
    $bdd = new PDO("pgsql:host=$host;port=$port;dbname=$dbname", $user, $password);
    $bdd->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Erreur de connexion : " . $e->getMessage());
}
?>