class Map:
    """All maps have the cabin as a safe zone, and a maximum of 8 players"""
    _safezone = "cabin"
    __max_players = 8
    _max_traitors = 3
    _max_survivors = 6
    current_season = "winter"
    def __init__(self, first_obj, second_obj, escape_method):
        """Each instantiated map will need a first objective, second objective, and an escape method for survivors"""
        self.first_obj = first_obj
        self.second_obj = second_obj
        self.escape_method = escape_method
        self.players = []
    
    @classmethod
    def _change_season(cls, season):
        """Allows us to change the season for all maps. Other functionality could be for holiday themed maps"""
        cls.current_season = season
    @classmethod
    def _alter_playercount(cls, players):
        """If we want to allow for more players on a map in the future for other gamemodes, we would use this function to set a new number of max players"""
        cls.__max_players = players
    
    def add_player(self, player):
        """add a player to the current map as long as the map has less than the max amount of players"""
        while len(self.players) <= Map.__max_players:
            self.players.append(player)
    
    def show_players(self):
        """print a list of the current players in the map"""
        for player in self.players:
            print(f"{player.name} has {player.current_hp} health left")
