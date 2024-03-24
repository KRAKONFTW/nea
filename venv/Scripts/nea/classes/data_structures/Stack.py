from classes.PlayerInventory import *

class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, level):
        self.stack.append(level)

    def pop(self):
        return self.stack.pop()