// * Definition for a binary tree node.
function TreeNode(val, left, right) {
  this.val = val === undefined ? 0 : val;
  this.left = left === undefined ? null : left;
  this.right = right === undefined ? null : right;
}

let searchResult = {};
const searchTree = async function (node, column, row) {
  let min_column = 0;
  let max_column = 0;
  console.log(node);
  console.log(column);
  if (node) {
    if (!searchResult.hasOwnProperty(column)) {
      console.log(`new column ${column}`);
      searchResult.column = [];
    }
    searchResult.column.push([row, node.val]);
    await searchTree(node.left, column - 1, row + 1);
    await searchTree(node.right, column + 1, row + 1);
    min_column = Math.min(min_column, column);
    max_column = Math.max(max_column, column);
  }
};

/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var verticalOrder = async function (root) {
  if (!root) {
    return [];
  }
  result = await searchTree(root, 0, 0);
  // console.log(result);
};

n1 = new TreeNode((val = 3), (left = undefined), (right = undefined));
n2 = new TreeNode((val = 11), (left = undefined), (right = undefined));
n3 = new TreeNode((val = 5), (left = undefined), (right = undefined));
n4 = new TreeNode((val = 4), (left = n1), (right = n2));
n5 = new TreeNode((val = 1), (left = undefined), (right = undefined));
n6 = new TreeNode((val = 7), (left = undefined), (right = undefined));
n7 = new TreeNode((val = 9), (left = n4), (right = undefined));
n8 = new TreeNode((val = 8), (left = n5), (right = n6));
root = new TreeNode((val = 2), (left = n7), (right = n8));
verticalOrder(root);
console.log(`:: searchResult ::`);
console.log(searchResult.column);
