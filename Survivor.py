from Player import Player
class Survivor(Player):
    starting_ability_charge = 100

    def __init__(self, name):
        """player role will be protected since it is good information to keep secret
        each survivor will start with full ability charge, and a defined role as Survivor"""
        super().__init__()
        self.name = name
        self._role = "Survivor"
        self.current_ability_charge = Survivor.starting_ability_charge

    @classmethod
    def set_ability_charge(cls, value):
        """Used to set starting ability charge to another value for possible different game modes"""
        cls.starting_ability_charge = value

    def use_ability(self, player):
        """Survivor ability heals other players. Watch out! If a survivor heals a traitor, it will heal them for double!"""
        if player._role == "Survivor":
            self.current_ability_charge = 0
            player.current_hp += 250
            print(f"{self.name} healed {player.name}")
        else:
            self.current_ability_charge = 0
            player.current_hp += 500
            print(f"{self.name} healed {player.name}")
    
    def die(self):
        print(f"{self.name} the {self._role} has perished!")

