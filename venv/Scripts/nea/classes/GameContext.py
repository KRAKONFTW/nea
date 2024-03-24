from classes.PlayerInventory import *

class GameContext(object):

    def __init__(self, player_name):
        self.player_name = player_name
        self.player_inventory = PlayerInventory()

    def get_player_name(self):
        return self.player_name

    def get_player_inventory(self):
        return self.player_inventory


