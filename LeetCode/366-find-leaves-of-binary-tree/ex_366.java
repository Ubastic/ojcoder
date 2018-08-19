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
    public List<List<Integer>> findLeaves(TreeNode root) {
        List<List<Integer>> list = new ArrayList<>();
        height(list, root);
        return list;
    }
    
    private int height(List<List<Integer>> list, TreeNode node) {
        if (node == null)   return -1;
        int level = 1 + Math.max(height(list, node.left), height(list, node.right));
        if (list.size() < level + 1)    list.add(new ArrayList<>());
        list.get(level).add(node.val);
        return level;
    }
}