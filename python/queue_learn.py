#there are a couple ways to implement queues in python
"""either with a regular list (not recommended)
list = []
list.append()
list.pop(1)


or with importing deque
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)  # Add to the rear

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()  # Remove from the front
        else:
            raise IndexError("Dequeue from an empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]  # Front item
        else:
            raise IndexError("Peek from an empty queue")

    def size(self):
        return len(self.items)

# Example usage:
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Output: 1
print(q.peek())     # Output: 2
print(q.size())     # Output: 2

"""

#but i think i will use queue
import queue

q = queue.Queue()

#enqueue
q.put(1)
q.put(2)
q.put(3)
q.put(4)
q.put(5)
print(q.get())

#dequeue
print(q.get())
print(q.get())
print(q.get())

print(q.qsize())    #returns the approximate size of the queue

#I think there is a direct link between linked lists and queues. So maybe I can use a queue without importing queue by using a linked list