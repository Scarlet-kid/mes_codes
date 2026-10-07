#!/bin/bash
recent=$(ls -t | head -n 1)
modifie=$(stat -c %y "$recent" | cut -d ' ' -f1)
echo "Le fichier le plus récent a été modifié le $modifie"

