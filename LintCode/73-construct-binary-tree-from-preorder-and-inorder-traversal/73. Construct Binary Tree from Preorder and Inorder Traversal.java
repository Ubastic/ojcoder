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
     *@param preorder : A list of integers that preorder traversal of a tree
     *@param inorder : A list of integers that inorder traversal of a tree
     *@return : Root of a tree
     */
    private TreeNode helper(HashMap<Integer, Integer> valToIndex, int[] preorder, int s1, int e1, int s2, int e2){
        if(s1 > e1 || s2 > e2) return null;
        
        int rootIndex = valToIndex.get(preorder[s2]);
        TreeNode root = new TreeNode(preorder[s2]);
        
        root.left = helper(valToIndex, preorder, s1, rootIndex - 1, s2 + 1, s2 + rootIndex - s1);
        root.right = helper(valToIndex, preorder, rootIndex + 1, e1, e2 - (e1 - rootIndex - 1), e2);
        
        return root;
    }
    
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        // write your code here
        if(inorder == null || inorder.length == 0) return null;
        
        HashMap<Integer, Integer> valToIndex = new HashMap<>();
        
        for(int i = 0; i < inorder.length; i++) valToIndex.put(inorder[i], i);
        
        return helper(valToIndex, preorder, 0, inorder.length - 1, 0, preorder.length - 1);
    }
}
