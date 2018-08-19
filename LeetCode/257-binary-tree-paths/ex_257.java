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
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> res = new ArrayList<>();
        helper(res, root, "");
        return res;
    }
    private void helper(List<String> res, TreeNode root, String path) {
        if (root == null)   return;
        path += Integer.toString(root.val);
        if (root.left == null && root.right == null) {
            res.add(path);
            return;
        }
        path += "->";
        helper(res, root.left, path);
        helper(res, root.right, path);
    }
}