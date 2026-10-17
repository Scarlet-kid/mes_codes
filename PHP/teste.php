<?php
$livres = [
    [
        'titre' => 'Dune',
        'auteur' => 'Frank Herbert',
        'annee' => 1965,
        'categorie' => 'Science-fiction'
    ],
    [
        'titre' => '1984',
        'auteur' => 'George Orwell',
        'annee' => 1949,
        'categorie' => 'Roman'
    ],
    [
        'titre' => 'Le petit prince',
        'auteur' => 'Antoine de Saint-Exupéry',
        'annee' => 1943,
        'categorie' => 'Roman'
    ]

];
$titre = $_POST['titre'] ?? null;
$auteur = $_POST['auteur'] ?? null;
$annee = $_POST['annee'] ?? null;
if($_SERVER['REQUEST_METHOD'] === 'POST')
{
    $livres[] = [
        'titre' => $titre,
        'auteur' => $auteur,
        'annee' => $annee
    ];
}

?>