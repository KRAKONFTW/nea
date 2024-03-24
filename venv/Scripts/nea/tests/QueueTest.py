import unittest

import sys
sys.path.append('../')

from classes.data_structures.Queue import *

class QueueTest(unittest.TestCase):

    def test_add_and_remove_from_queue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)

if __name__ == '__main__':
    unittest.main()

