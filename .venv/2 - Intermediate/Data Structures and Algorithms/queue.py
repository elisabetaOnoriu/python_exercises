class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def __repr__(self):
        return f"Queue({self.items})"


q = Queue()
q.enqueue("A")
q.enqueue("B")
print(q)
print(q.dequeue())
print(q)
