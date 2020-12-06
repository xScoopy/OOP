class Player:
    _starting_hp = 1000
    _starting_warmth = 100
    _starting_hunger = 0

    def __init__(self):
        """each player will be instantiated with the following values: 
        hp = hit points/health
        warmth = heat level that will gradually deplete while outside
        hunger = increasing value that will be addressed by eating food
        items = items that players can hold onto such as berries or weapons"""
        self.current_hp = Player._starting_hp
        self.current_warmth = Player._starting_warmth
        self.current_hunger = Player._starting_hunger
        self.items = []
        self.location = "cabin"

    @classmethod
    def __set_startinghp(cls, starting_value):
        """used to alter the starting hp for seasonal game modes. Protected method since we won't want this accessible due to cheating concerns. """
        cls._starting_hp = starting_value

    @classmethod
    def __set_startinghunger(cls, starting_value):
        """used to alter starting hunger for seasonal game modes Protected method since we won't want this accessible due to cheating concerns. """
        cls._starting_hunger = starting_value

    def is_outside(self, location):
        """hypothetical method to gradually decrease warmth and increase hunger while the player is away from the cabin"""
        while self.location != "cabin":
            if self.current_hunger < 100 and self.current_warmth > 0 and self.current_hp > 0:
                self.current_hunger += 0.5
                self.current_warmth -= 0.5
            else:
                self.die()

    def die(self):
        print("The player is dead")

    def eat_berry(self):
        """Player eats the berry to reduce their hunger level. Checks the player items for a berry before eating. will not reduce hunger below zero"""
        if "berry" in self.items:
            if self.current_hunger > 10:
                self.current_hunger -= 10
                self.items.remove("berry")
                print("Berry eaten")
            else:
                self.current_hunger = 0
                print("Berry eaten")
        else:
            print(f"{self.name} doesn't have a berry")
