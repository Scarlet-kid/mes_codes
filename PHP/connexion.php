<?php
    $dbname = 'postgres';
    $host = 'localhost';
    $user = 'postgres';
    $password = '66793270';
    $port = 5432;

    $dsn = "pgsql:host=$host;port=$port;dbname=$dbname";
    $pdo = new PDO($dsn, $user, $password);
    $pdo->setAttribute(PDO::ATTR_ERRMODE,PDO::ERRMODE_EXCEPTION);
?>