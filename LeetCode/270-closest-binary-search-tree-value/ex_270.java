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
    public int closestValue(TreeNode root, double target) {
        int closest = root.val;
        TreeNode node = root;
        while (node != null) {
            closest = Math.abs(node.val - target) < Math.abs(closest - target) ? node.val : closest;
            node = node.val > target ? node.left : node.right;
        }
        return closest;
    }
}