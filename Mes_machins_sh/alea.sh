echo $RANDOM
read -p "Saisir un entier positif:" max
echo $(( $RANDOM % max ))
