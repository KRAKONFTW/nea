from classes.levels.Level import *
from classes.data_structures.Queue import *

class LevelCreator(object):

    def __init__(self):
        self.level_queue = Queue()

    def create_levels(self):
        self.level_queue.enqueue(
            Level("Phantasm",
                [
                    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
                    "W                            W",
                    "W                            W",
                    "W                   QQQQQQ   W",
                    "W                   Q        W",
                    "W                   Q        W",
                    "W                   Q     EE W",
                    "W                   WWWWWWWWWWW",
                    "WWWWWWWWWWWw                 W",
                    "W                            W",
                    "W     WW   WWWWW     WWWWWWWWW",
                    "W                            W",
                    "WWW  WWWWWWWWWWW             W",
                    "W                            W",
                    "W                            W",
                    "W                            W",
                    "W                            W",
                    "W           J                W",
                    "W                            W",
                    "W                            W",
                    "W                            W",
                    "WWWWWWWWW               WWWWWW",
                    "W                            W",
                    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
                ]))

        self.level_queue.enqueue(
            Level("Slaughterhouse",
                  [
                    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
                    "W       J               W    W",
                    "W                       W    W",
                    "W    WWWW   WWWWW   WWWWW    W",
                    "W    W          W       W    W",
                    "W    W      J           W   WW",
                    "W    W   WW                  W",
                    "W    W    W     WWWW         W",
                    "W  J  WWW  W     W  W        W",
                    "W         W       EE         W",
                    "WWWW      WWWWWWWWWWWWWW WWWWW",
                    "W  W     WW                  W",
                    "W       WW                   W",
                    "W             WWW            W",
                    "W   WW               WW  WWW W",
                    "W    W  WWW          WWWWWWW W",
                    "W    W    W   WWW       WW   W",
                    "W    WW   W                  W",
                    "W     W   W          WWWWWWWWW",
                    "WWWW      WWWWW      WW  WWW W",
                    "W  W      W                W W",
                    "W  W   WWWW     W  W       W W",
                    "W      W           W  WWW  W W",
                    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"] ))

        self.level_queue.enqueue(
            Level("The Gauntlet", [
                    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
                    "W   W     W        W  W      W",
                    "W    W   WWW           W    WWW",
                    "W    WWW     WWWWWWWWWW      W",
                    "W    W       W               W",
                    "W    W    WWWW        WWWWWW W",
                    "WJ   W                   W   W",
                    "W     W  J    WWW            W",
                    "WW    W        W      W EE   W",
                    "WW                          WW",
                    "W         W        W         W",
                    "W    W WWWWWWWWWWW WWWWWWWWWWW",
                    "W    W   W         W         W",
                    "W    W   W         W         W",
                    "W    W             W     W   W",
                    "W    W   W         W     W   W",
                    "W    W   W         W     W   W",
                    "W J  W   W         W     W   W",
                    "W    W   W J       W     W   W",
                    "W    W   W         W     W   W",
                    "W        W         W     W   W",
                    "W    W   W     J         WEE W",
                    "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
            ]))

        self.level_queue.enqueue(
            Level("Blood Bath",
                  [
                "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
                "W                            W",
                "W                            W",
                "W                   QQQQQQ   W",
                "W                   Q        W",
                "W                   Q        W",
                "W         J         Q        W",
                "W                   WWWWWWWWWWW"
                "WWWWWWWWWWWw                 W",
                "W                            W",
                "W     WWWWWWWWWWW      WWWWWWW",
                "W                            W",
                "WWWWWWWWWWWWWWWW             W",
                "W                            W",
                "W                            W",
                "W        WWWWWWWWWWWWWWWWWWWWW",
                "W        W                   W",
                "W        Q      EE           W",
                "W        WWWWWWWWWWWW        W",
                "W                            W",
                "W                    W       W",
                "WWWWWWWWW            WWWWWWWWW",
                "W                            W",
                "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
            ]))

        self.level_queue.enqueue(
            Level("Sacramento's Lair", [
                "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
                "W                            W",
                "W                            W",
                "W                   QQQQQQ   W",
                "W                   Q        W",
                "W      J            Q        W",
                "W                   Q        W",
                "W                   WWWWWWWWWWW"
                "WWWWWWWWWWWw                 W",
                "W                            W",
                "W     WWWWWWWWWWW      WWWWWWW",
                "W                            W",
                "WWWWWWWWWWWWWWWW             W",
                "W                            W",
                "W                            W",
                "W        WWWWWWWWWWWWWWWWWWWWW",
                "W        W                   W",
                "W        Q      EE           W",
                "W        WWWWWWWWWWWW        W",
                "W                            W",
                "W                    W       W",
                "WWWWWWWWW            WWWWWWWWW",
                "W                            W",
                "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
            ]))

        self.level_queue.enqueue(
            Level("Sacramento's Basement", [
                "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW",
                "W                            W",
                "W                            W",
                "W                   QQQQQQ   W",
                "W         J         Q        W",
                "W                   Q        W",
                "W                   Q        W",
                "W                   WWWWWWWWWWW"
                "WWWWWWWWWWWw                 W",
                "W                            W",
                "W     WWWWWWWWWWW      WWWWWWW",
                "W                            W",
                "WWWWWWWWWWWWWWWW             W",
                "W                            W",
                "W                            W",
                "W        WWWWWWWWWWWWWWWWWWWWW",
                "W        W                   W",
                "W        Q      EE           W",
                "W        WWWWWWWWWWWW        W",
                "W                            W",
                "W                    W       W",
                "WWWWWWWWW            WWWWWWWWW",
                "W                            W",
                "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"

            ]))

        return self.level_queue
