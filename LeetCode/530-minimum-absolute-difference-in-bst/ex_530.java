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
    int min = 0x7fffffff;
    int prev = -1;
    public int getMinimumDifference(TreeNode root) {
        if (root == null)   return min;
        getMinimumDifference(root.left);
        if (prev != -1)     min = Math.min(min, root.val - prev);
        prev = root.val;
        getMinimumDifference(root.right);
        return min;
    }
}