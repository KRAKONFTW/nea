import unittest

import sys
sys.path.append('../')

from classes.data_structures.Stack import *

class StackTest(unittest.TestCase):

    def test_add_and_remove_from_stack(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

if __name__ == '__main__':
    unittest.main()

