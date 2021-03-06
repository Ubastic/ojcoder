package CloneBinaryTree;

import Common.TreeNode;

/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param root: The root of binary tree
     * @return root of new tree
     */
    public TreeNode cloneTree(TreeNode root) {
        // Write your code here
        if(root == null)
            return null;

        TreeNode copy = new TreeNode(root.val);
        TreeNode left_copy = cloneTree(root.left);
        TreeNode right_copy = cloneTree(root.right);
        copy.left = left_copy;
        copy.right = right_copy;

        return copy;
    }
}