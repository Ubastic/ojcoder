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
     * @param value: Remove the node with given value.
     * @return: The root of the binary search tree after removal.
     */
    private void swap(TreeNode p1, TreeNode p2){
        int tmp = p1.val;
        p1.val = p2.val;
        p2.val = tmp;
    } 
    
    public TreeNode removeNode(TreeNode root, int value) {
        // write your code here
        if(root == null) return root;
        
        if(root.val > value) root.left = removeNode(root.left, value);
        
        else if(root.val < value) root.right = removeNode(root.right, value);
        
        else{
            if(root.left == null && root.right == null) return null;
            
            else if(root.left != null){
                TreeNode p = root.left;
                
                while(p.right != null) p = p.right;
                
                swap(root, p);
                
                root.left = removeNode(root.left, value);
            }else{
                TreeNode p = root.right;
                
                while(p.left != null) p = p.left;
                
                swap(root, p);
                
                root.right = removeNode(root.right, value);
            }
        }
        
        return root;
    }
}
