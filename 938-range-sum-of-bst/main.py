from typing import Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        else:
            return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)


n6 = TreeNode(val=18)
n4 = TreeNode(val=7)
n3 = TreeNode(val=3)
n2 = TreeNode(val=15, right=n6)
n1 = TreeNode(val=5, left=n3, right=n4)
root = TreeNode(val=10, left=n1, right=n2)

sln = Solution()


print(sln.rangeSumBST(root, 7, 15))  # 32
assert sln.rangeSumBST(root, 7, 15) == 32

n8 = TreeNode(val=6)
n7 = TreeNode(val=1)
n6 = TreeNode(val=18)
n5 = TreeNode(val=13)
n4 = TreeNode(val=7, left=n8)
n3 = TreeNode(val=3, left=n7)
n2 = TreeNode(val=15, right=n6)
n1 = TreeNode(val=5, left=n3, right=n4)
root = TreeNode(val=10, left=n1, right=n2)

print(sln.rangeSumBST(root, 6, 10))  # 23
assert sln.rangeSumBST(root, 6, 10) == 23
