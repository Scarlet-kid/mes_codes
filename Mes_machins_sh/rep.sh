#!/bin/bash
read -p "Saisir le nom du répertoire:" nomRep
if [[ -e $nomRep ]]; then
	echo le répertoire $nomRep existe déjà
else
	mkdir $nomRep
fi
