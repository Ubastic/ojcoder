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
    public int sumOfLeftLeaves(TreeNode root) {
        int res = 0;
        if (root != null) {
            if (root.left != null && root.left.left == null && root.left.right == null) {
                res += root.left.val;
            }
            res += sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right);
        }
        return res;
    }
}