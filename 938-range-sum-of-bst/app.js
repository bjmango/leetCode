//  Definition for a binary tree node.
function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

/**
 * @param {TreeNode} root
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var rangeSumBST = function (root, low, high) {
  if (!root) {
    return 0;
  }
  if (low <= root.val && root.val <= high) {
    return root.val + rangeSumBST(root.left, low, high) + rangeSumBST(root.right, low, high);
  } else if (root.val < low) {
    return rangeSumBST(root.right, low, high);
  } else if (root.val > high) {
    return rangeSumBST(root.left, low, high);
  }
};

n6 = new TreeNode((val = 18));
n4 = new TreeNode((val = 7));
n3 = new TreeNode((val = 3));
n2 = new TreeNode((val = 15), (right = n6));
n1 = new TreeNode((val = 5), (left = n3), (right = n4));
root = new TreeNode((val = 10), (left = n1), (right = n2));

console.log(rangeSumBST(root, 7, 15)); //32

n8 = new TreeNode((val = 6));
n7 = new TreeNode((val = 1));
n6 = new TreeNode((val = 18));
n5 = new TreeNode((val = 13));
n4 = new TreeNode((val = 7), (left = n8));
n3 = new TreeNode((val = 3), (left = n7));
n2 = new TreeNode((val = 15), (right = n6));
n1 = new TreeNode((val = 5), (left = n3), (right = n4));
root = new TreeNode((val = 10), (left = n1), (right = n2));

console.log(rangeSumBST(root, 6, 10)); // 23
