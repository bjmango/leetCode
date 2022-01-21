from typing import List, Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verticalOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []

    search_result = defaultdict(list)
    min_column = max_column = 0

    def search_tree(node, column, row):
        if node is not None:
            nonlocal min_column, max_column
            search_result[column].append([row, node.val])
            search_tree(node.left, column - 1, row + 1)
            search_tree(node.right, column + 1, row + 1)
            min_column = min(min_column, column)
            max_column = max(max_column, column)

    search_tree(root, 0, 0)
    result = []
    for col in range(min_column, max_column + 1):
        search_result[col].sort(key=lambda x: x[0])
        values = [val for row, val in search_result[col]]
        result.append(values)
    return result
    # if root is None:
    #     return []

    # search_result = defaultdict(list)
    # min_column = max_column = 0

    # def tree_search(node, column, row):
    #     if node is not None:
    #         nonlocal min_column, max_column
    #         search_result[column].append((row, node.val))
    #         tree_search(node.left, column - 1, row + 1)
    #         tree_search(node.right, column + 1, row + 1)
    #         min_column = min(min_column, column)
    #         max_column = max(max_column, column)

    # tree_search(root, 0, 0)

    # ret = []
    # for col in range(min_column, max_column + 1):
    #     search_result[col].sort(key=lambda x: x[0])
    #     values = [val for row, val in search_result[col]]
    #     ret.append(values)
    # return ret


n1 = TreeNode(val=3, left=None, right=None)
n2 = TreeNode(val=11, left=None, right=None)
n3 = TreeNode(val=5, left=None, right=None)
n4 = TreeNode(val=4, left=n1, right=n2)
n5 = TreeNode(val=1, left=None, right=None)
n6 = TreeNode(val=7, left=None, right=None)
n7 = TreeNode(val=9, left=n4, right=None)
n8 = TreeNode(val=8, left=n5, right=n6)
root = TreeNode(val=2, left=n7, right=n8)


print(verticalOrder(root))
