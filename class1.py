class Map:
    """All maps have the cabin as a safe zone, and a maximum of 8 players"""
    safezone = "cabin"
    max_players = 8
    def __init__(self, first_obj, second_obj, escape_method):
        """Each instantiated map will need a first objective, second objective, and an escape method for survivors"""
        self.first_obj = first_obj
        self.second_obj = second_obj
        self.escape_method = escape_method
        self.players = []