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
     * @param root: The root of the binary search tree.
     * @param A and B: two nodes in a Binary.
     * @return: Return the least common ancestor(LCA) of the two nodes.
     */
    private List<TreeNode> pathA = new ArrayList<>(), pathB = new ArrayList<>();
     
    private void helper(TreeNode node, TreeNode A, TreeNode B, List<TreeNode> path){
        if(node == null) return;
        
        if(node == A && node == B){
            pathA.addAll(path);
            pathA.add(node);
            pathB.addAll(path);
            pathB.add(node);
            return;
        }else if(node == A){
            pathA.addAll(path);
            pathA.add(node);
        }else if(node == B){
            pathB.addAll(path);
            pathB.add(node);
        }
        
        path.add(node);
        helper(node.left, A, B, path);
        helper(node.right, A, B, path);
        path.remove(path.size() - 1);
    } 
     
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode A, TreeNode B) {
        // write your code here
        helper(root, A, B, new ArrayList<TreeNode>());
        
        int index = 0;
        
        while(index < pathA.size() && index < pathB.size() && pathA.get(index) == pathB.get(index)) index++;
        
        return pathA.get(index - 1);
    }
}
