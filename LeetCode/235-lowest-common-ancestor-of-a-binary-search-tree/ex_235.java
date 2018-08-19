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
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode small = p.val <= q.val ? p : q;
        TreeNode large = q.val > p.val ? q : p;
        TreeNode commonAncestor = root;
        while (commonAncestor.val < small.val || commonAncestor.val > large.val) {
            while (commonAncestor.val < small.val)
                commonAncestor = commonAncestor.right;
            while (commonAncestor.val > large.val)
                commonAncestor = commonAncestor.left;
        }
        return commonAncestor;
    }
}