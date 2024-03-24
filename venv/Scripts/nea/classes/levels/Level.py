class Level(object):

    def __init__(self, level_name, level_map):
        self.level_name = level_name
        self.level_map = level_map

    def get_level_map(self):
        return self.level_map

    def get_level_name(self):
        return self.level_name