#!/bin/bash
for element in * ; do
	if [[ -f $element ]]; then
		echo $element est un fichier
	elif [[ -d $element ]]; then
		echo $element est un répertoire
	else
		echo $element "est d'un autre type"
	fi
done
