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
     *@param inorder : A list of integers that inorder traversal of a tree
     *@param postorder : A list of integers that postorder traversal of a tree
     *@return : Root of a tree
     */
    private TreeNode helper(HashMap<Integer, Integer> valToIndex, int[] postorder, int s1, int e1, int s2, int e2){
        if(s1 > e1 || s2 > e2) return null;
        
        int rootIndex = valToIndex.get(postorder[e2]);
        TreeNode root = new TreeNode(postorder[e2]);
        
        root.left = helper(valToIndex, postorder, s1, rootIndex - 1, s2, s2 + rootIndex - 1 - s1);
        root.right = helper(valToIndex, postorder, rootIndex + 1, e1, e2 - 1 - (e1 - rootIndex - 1), e2 - 1);
        
        return root;
    } 
     
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        // write your code here
        if(inorder == null || inorder.length == 0) return null;
        
        HashMap<Integer, Integer> valToIndex = new HashMap<>();
        
        for(int i = 0; i < inorder.length; i++) valToIndex.put(inorder[i], i);
        
        return helper(valToIndex, postorder, 0, inorder.length - 1, 0, postorder.length - 1);
    }
}
