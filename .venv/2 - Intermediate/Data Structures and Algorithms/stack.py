class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __repr__(self):
        return f"Stack({self.items})"


s = Stack()
s.push(1)
s.push(2)
print(s)
print(s.pop())
print(s)
