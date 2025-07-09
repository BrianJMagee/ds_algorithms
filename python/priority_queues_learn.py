import queue

#priority queues no longer are strictly fifo or lifo
#you can give every element a certain priority by passing a tuple

q = queue.PriorityQueue()

q.put((2, "Hello, world"))  #need to pass as a tuple
q.put((100, "apple"))   #100 is the least priority, 1 is the most
q.put((1, "Orange"))

while not q.empty():
    print(q.get())