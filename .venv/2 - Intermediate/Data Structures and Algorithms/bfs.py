from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []


def bfs(root):
    if not root:
        return []

    queue = deque([root])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.val)

        for child in node.children:
            queue.append(child)

    return result


a = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")

a.children = [b, c, d]
c.children = [e]

print(bfs(a))
