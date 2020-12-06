from Map import Map
from Player import Player
from Survivor import Survivor
from Traitor import Traitor

# instantiation of map class:
example_map = Map("repair", "wolf defense", "helicopter")

# instantiation of Player object:
# disclaimer: Player object is not really meant to be instantiated, but moreso to contain the all encompassing attributes and methods of all players. The survivors and traitors are the ones that will be instantiated into actual objects for gameplay.

example_player = Player()

# instantiation of Survivor and Traitor objects

player1 = Survivor("Jeremiah")
player2 = Traitor("Jacob")

# adding the players to the map

example_map.add_player(player1)
example_map.add_player(player2)

# showing players on the current map

example_map.show_players()

#example of overriding the die() method

example_player.die()
player1.die()
player2.die()
