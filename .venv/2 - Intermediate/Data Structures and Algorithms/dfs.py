class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []


def dfs(root):
    result = []

    def dfs_helper(node):
        if not node:
            return
        result.append(node.val)
        for child in node.children:
            dfs_helper(child)

    dfs_helper(root)
    return result


a = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
d = TreeNode("D")
e = TreeNode("E")

a.children = [b, c, d]
c.children = [e]

print(dfs(a))
