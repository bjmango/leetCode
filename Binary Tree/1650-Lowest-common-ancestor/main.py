class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


def lowestCommonAncestor(p: "Node", q: "Node") -> "Node":
    path_to_root = []

    def search_path_to_root(node):
        if node.parent is not None:
            search_path_to_root(node.parent)
        path_to_root.append(node)
        return path_to_root

    p_path = search_path_to_root(p)
    path_to_root = []
    q_path = search_path_to_root(q)

    # print([cp.val for cp in p_path])
    # print([cq.val for cq in q_path])

    length = min(len(p_path), len(q_path))
    for i in range(length):
        if p_path[i].val != q_path[i].val:
            return p_path[i - 1]
    return p_path[length - 1]


# region
n1 = Node(3)
n2 = Node(5)
n3 = Node(1)
n4 = Node(6)
n5 = Node(2)
n6 = Node(0)
n7 = Node(8)
n8 = Node(7)
n9 = Node(4)
n1.left = n2
n1.right = n3
n1.parent = None
n2.left = n4
n2.right = n5
n2.parent = n1
n3.left = n6
n3.right = n7
n3.parent = n1
n4.left = None
n4.right = None
n4.parent = n2
n5.left = n8
n5.right = n9
n5.parent = n2
n6.left = None
n6.right = None
n6.parent = n3
n7.left = None
n7.right = None
n7.parent = n3
n8.left = None
n8.right = None
n8.parent = n5
n9.left = None
n9.right = None
n9.parent = n5
# endregion
print(lowestCommonAncestor(n3, n2).val)
