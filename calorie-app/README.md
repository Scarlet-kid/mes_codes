# À table

PWA en français pour composer un repas et obtenir une estimation de ses calories à partir des aliments et quantités saisis.

## Lancer en local

Le service worker (mode hors ligne) et l’installation PWA nécessitent `localhost` ou un site servi en HTTPS. Depuis le dossier `calorie-app`, lancez par exemple :

```sh
python -m http.server 8000
```

Ouvrez ensuite `http://localhost:8000`. Aucun compte, serveur applicatif ou service d’IA n’est utilisé. Les repas et aliments personnalisés sont stockés dans le stockage local du navigateur, sur cet appareil.

## Utiliser sur un téléphone

Pour l’ouvrir et l’installer sur un téléphone, hébergez le contenu de ce dossier sur un site HTTPS, puis ouvrez son adresse avec le navigateur du téléphone. Choisissez ensuite « Ajouter à l’écran d’accueil » (Safari) ou « Installer l’application » (navigateurs compatibles). HTTPS est nécessaire pour l’installation PWA et le fonctionnement hors ligne ; le serveur local ci-dessus sert au développement sur ordinateur.

Les données sont propres au navigateur et à l’appareil utilisés : elles ne sont ni synchronisées entre appareils ni sauvegardées sur un serveur.

## Fonctionnalités

- Recherche et filtres dans un petit catalogue d’aliments courants.
- Quantités modifiables en grammes et total calorique estimé.
- Ajout d’aliments personnalisés à partir de la valeur nutritionnelle pour 100 g.
- Enregistrement et réouverture des repas sur l’appareil.
- Interface responsive, installable et utilisable hors ligne après le premier chargement.

Les valeurs du catalogue sont indicatives et peuvent varier selon les aliments, marques, portions et modes de préparation. Les calories calculées ne sont pas un avis médical ni une mesure exacte.
