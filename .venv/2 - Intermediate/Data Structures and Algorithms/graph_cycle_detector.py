class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return f"Node({self.name})"


class GraphCycleDetector:
    def __init__(self):
        self.visited = set()
        self.recursion_stack = set()

    def has_cycle(self, node):
        if node in self.recursion_stack:
            return True

        if node in self.visited:
            return False

        self.visited.add(node)
        self.recursion_stack.add(node)

        for child in node.children:
            if self.has_cycle(child):
                return True

        self.recursion_stack.remove(node)
        return False


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

a.add_child(b)
a.add_child(c)
b.add_child(d)

detector = GraphCycleDetector()
print("Has cycle:", detector.has_cycle(a))


x = Node("X")
y = Node("Y")
z = Node("Z")

x.add_child(y)
y.add_child(z)
z.add_child(x)

detector = GraphCycleDetector()
print("Has cycle:", detector.has_cycle(x))
