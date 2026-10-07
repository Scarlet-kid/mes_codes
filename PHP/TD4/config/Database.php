<?php
namespace Config;

use PDO;
use PDOException;

class Database {
    private string $host = 'iutinfo-sgbd.uphf.fr';
    private string $port = '5432';
    private string $dbname = 'iutinfo573';
    private string $user = 'iutinfo573';
    private string $password = 'idhaGxeW';
    private ?PDO $conn = null;

    public function getConnection(): PDO {
        if ($this->conn === null) {
            try {
                $dsn = "pgsql:host={$this->host};port={$this->port};dbname={$this->dbname}";
                $this->conn = new PDO($dsn, $this->user, $this->password, [
                    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
                    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC
                ]);
            } catch (PDOException $e) {
                die("Erreur de connexion : " . $e->getMessage());
            }
        }
        return $this->conn;
    }
}