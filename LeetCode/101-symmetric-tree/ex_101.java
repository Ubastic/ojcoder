/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean isSymmetric(TreeNode root) {
        return root == null || checkSymmetric(root.left, root.right);
    }
    
    private boolean checkSymmetric(TreeNode left, TreeNode right) {
        if (left == null && right == null)  return true;
        if (left == null || right == null)  return false;
        return left.val == right .val && checkSymmetric(left.left, right.right) && checkSymmetric(right.left, left.right);
    }
}