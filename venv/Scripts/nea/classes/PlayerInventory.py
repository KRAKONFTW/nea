class PlayerInventory(object):

    def __init__(self):
        self.inventory = []

    # move the player object by dx across the x-axis or dy across the y-axis
    def add_jewel(self, jewel):
        self.inventory.append(jewel)

    def get_total_items(self):
        return len(self.inventory)