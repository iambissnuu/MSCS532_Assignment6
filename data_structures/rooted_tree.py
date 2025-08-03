class TreeNode:
    def __init__(self, value):
        self.data = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def traverse(self, level=0):
        print("  " * level + str(self.data))
        for child in self.children:
            child.traverse(level + 1)

if __name__ == "__main__":
    root = TreeNode("A")
    b = TreeNode("B")
    c = TreeNode("C")
    d = TreeNode("D")
    e = TreeNode("E")
    f = TreeNode("F")

    root.add_child(b)
    root.add_child(c)
    b.add_child(d)
    b.add_child(e)
    c.add_child(f)

    print("Rooted Tree:")
    root.traverse()
