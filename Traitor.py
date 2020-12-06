from Player import Player
class Traitor(Player):
    starting_ability_charge = 0

    def __init__(self, name):
        """player role will be protected since it is good information to keep secret
        each traitor will start with full ability charge, and a defined role as Traitor"""
        super().__init__()
        self.name = name
        self._role = "Traitor"
        self.current_ability_charge = Traitor.starting_ability_charge

    @classmethod
    def set_ability_charge(cls, value):
        """Used to set starting ability charge to another value for possible different game modes"""
        cls.starting_ability_charge = value

    def use_ability(self, player):
        """Traitor ability poisons other players. Watch out! If a traitor poisons a traitor, it will instantly kill them!"""
        if self.current_ability_charge == 100:
            if player._role == "Survivor":
                self.current_ability_charge = 0
                player.current_hp -= 100
                player.current_hunger += 25
                print(f"{self.name} poisoned {player.name}")
            else:
                self.current_ability_charge = 0
                player.current_hp = 0
                print(f"{self.name} killed {player.name}!")
    
    def die(self):
        print(f"{self.name} the {self._role} has perished! Good Riddance.")
