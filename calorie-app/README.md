# À table

PWA en français pour tenir un journal alimentaire, suivre les calories estimées et comparer une tendance théorique avec les pesées réelles.

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

- Navigation par onglets entre les repas, le bilan mensuel, l’activité et l’historique.
- Recherche et filtres dans un petit catalogue d’aliments courants.
- Quantités modifiables en grammes et total calorique estimé.
- Ajout d’aliments personnalisés à partir de la valeur nutritionnelle pour 100 g.
- Journal des repas par date avec cumul quotidien des calories.
- Profil adulte permettant d’estimer une dépense quotidienne et de proposer un objectif indicatif.
- Bilan mensuel en graphiques : apports quotidiens, tendance théorique et pesées saisies.
- Déclaration des séances de musculation par date, type (Push, Pull, Abdo-jambe), durée et intensité.
- Ajustement indicatif de l’objectif journalier et de la tendance énergétique les jours de musculation déclarés.
- Saisie manuelle des pas par jour, objectif de pas modifiable (8 000 par défaut) et graphique mensuel.
- Confirmation explicite des journées complètes avant de les inclure dans la tendance théorique.
- Enregistrement et réouverture des repas, du profil, des pesées et des pas sur l’appareil.
- Interface responsive, installable et utilisable hors ligne après le premier chargement.

Les pas sont saisis manuellement : la PWA ne lit pas les capteurs, Apple Santé ou Health Connect. Ils sont suivis séparément et ne sont pas convertis en calories ni utilisés pour modifier l’estimation de dépense ou de déficit.

La dépense quotidienne est estimée à partir de la formule de Mifflin-St Jeor et d’un coefficient d’activité choisi par l’utilisateur ; elle reste approximative. Le choix « autre / préfère ne pas préciser » utilise un ajustement moyen approximatif. Un déficit indicatif de 250 kcal n’est proposé que si la dépense calculée atteint au moins 1 750 kcal/j ; sinon, l’objectif affiché est la dépense estimée. Cela ne constitue pas un avis médical ni une prescription. Le profil et les estimations sont destinés aux adultes et ne conviennent pas pour gérer une grossesse, un problème de santé ou un trouble alimentaire sans accompagnement professionnel.

Les séances utilisent le [Compendium of Physical Activities 2024](https://pacompendium.com/conditioning-exercise/) : musculation avec plusieurs exercices et résistances variées (code 02054, 3,5 MET) ou musculation vigoureuse / bodybuilding (code 02050, 6 MET). La répartition Push/Pull/Abdo-jambe décrit le type de séance, mais ne suffit pas à déduire son intensité. L’estimation de calories actives est `(MET - 1) × poids en kg × durée en heures`, basée sur la définition du MET du [Compendium](https://pacompendium.com/). À titre d’exemple, 75 kg pendant 60 minutes donne environ 188 kcal à 3,5 MET ou 375 kcal à 6 MET. Les valeurs varient selon les personnes et la séance réelle ; elles ne sont ni une mesure individuelle ni une prescription.

Pour limiter le double comptage, choisissez dans le profil votre activité habituelle hors séances de musculation ; seules les séances consignées séparément sont ajoutées au repère du jour. L’estimation utilise la dernière pesée connue à la date de la séance, ou le poids du profil si aucune pesée antérieure n’existe. Les pas restent distincts, ne sont pas convertis en calories et ne modifient pas le calcul.

La variation théorique suppose une dépense constante et convertit le bilan énergétique des seules journées marquées complètes avec le facteur approximatif de 7 700 kcal/kg. Les repas oubliés, les pas, les autres activités, les variations d’eau, la digestion et de nombreux autres facteurs ne sont pas modélisés. Le calcul ne prédit donc pas le poids réel : seules les pesées enregistrées sont des mesures, et même celles-ci varient naturellement.
