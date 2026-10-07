<?php
namespace App\Modele;

class Livre {
    private ?int $id; //int ou null
    private string $titre;
    private ?int $annee;
    private int $auteurId;
    private ?string $auteurNom;

    public function __construct(string $titre, int $auteurId, ?int $annee = null, ?int $id = null, ?string $auteurNom = null) {
        $this->id = $id;
        $this->titre = $titre;
        $this->annee = $annee;
        $this->auteurId = $auteurId;
        $this->auteurNom = $auteurNom;
    }

    public function getId(): ?int { return $this->id; } // renvoie un int ou un null
    public function getTitre(): string { return $this->titre; }
    public function getAnnee(): ?int { return $this->annee; }
    public function getAuteurId(): int { return $this->auteurId; }
    public function getAuteurNom(): ?string { return $this->auteurNom; }
}