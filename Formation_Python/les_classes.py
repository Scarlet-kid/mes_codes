from Model.player import Player
from Model.weapon import Weapon

# A partir d'un setteur,on peut affecter a una variable qui se trouve dans une classe un objet qu'on aura créer.

knife = Weapon("couteau",2)
player1= Player("Sosthène",29,15)
player1.set_weapon(knife)
player2 = Player("Eddy",29,15)
player1.attack_player(player2)
print(player1.get_pseudo(),'attaque',player2.get_pseudo())
print("Bienvenue au joueur",player1.get_pseudo(),'/ Point de vie:',player1.get_health(),'/ attaque:',player1.get_attack())
print("Bienvenue au joueur",player2.get_pseudo(),'/ Point de vie:',player2.get_health(),'/ attaque:',player2.get_attack())