class Queue(object):

    def __init__(self):
        self.queue = []

    def enqueue(self, level):
        # Append to the end of the queue
        self.queue.append(level)

    def dequeue(self):
        # Remove the item from the head of the queue
        return self.queue.pop(0)