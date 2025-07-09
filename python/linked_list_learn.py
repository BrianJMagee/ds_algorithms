"""
I should implement this myself at some point

Good question — **linked lists** are fundamental data structures, but unlike stacks, queues, and heaps, Python doesn’t have a built-in linked list class.
However, you can implement them easily using custom classes.

---

## ✅ **What is a linked list?**

A **linked list** is a collection of nodes where each node stores:

* some **data**
* a **reference** (pointer) to the next node

The simplest type is a **singly linked list** (each node points only to the next).
More advanced is a **doubly linked list** (each node points to **next** and **previous**).

---

## ✅ **Singly Linked List Example**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        current = self.head

        # Deleting head node
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            return  # Key not found

        prev.next = current.next
        current = None

    def display(self):
        elems = []
        current = self.head
        while current:
            elems.append(current.data)
            current = current.next
        print("Linked List:", elems)

# Example usage:
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.prepend(0)
ll.display()  # Linked List: [0, 1, 2, 3]
ll.delete(2)
ll.display()  # Linked List: [0, 1, 3]
```

---

## ✅ **Doubly Linked List**

A **doubly linked list** has `prev` and `next` pointers:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def display_forward(self):
        elems = []
        curr = self.head
        while curr:
            elems.append(curr.data)
            curr = curr.next
        print("Forward:", elems)

    def display_backward(self):
        elems = []
        curr = self.head
        while curr and curr.next:
            curr = curr.next  # Move to tail

        while curr:
            elems.append(curr.data)
            curr = curr.prev
        print("Backward:", elems)

# Example usage:
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.display_forward()   # Forward: [1, 2, 3]
dll.display_backward()  # Backward: [3, 2, 1]
```

---

## ✅ **Notes**

* Python’s `list` is *not* a linked list — it’s a dynamic array.
* Linked lists make sense when:

  * You have lots of insertions/deletions in the middle.
  * You want O(1) insert/delete when you already have the node.
* For general use, Python’s `list` or `deque` is almost always more practical.

---

If you want, I can show:

* Circular linked lists
* Implementing advanced operations (reversing, sorting, detecting loops)
* Using `collections.OrderedDict` as a linked-list-like structure

Just ask!
"""