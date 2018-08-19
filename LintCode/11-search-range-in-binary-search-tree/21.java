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
     * @param k1 and k2: range k1 to k2.
     * @return: Return all keys that k1<=key<=k2 in ascending order.
     */
    private ArrayList<Integer> ans = new ArrayList<>();
    
    private void inorder(TreeNode root, int k1, int k2){
        if(root == null) return;
        
        if(root.val > k2) inorder(root.left, k1, k2);
        
        else if(root.val < k1) inorder(root.right, k1, k2);
        
        else{
            inorder(root.left, k1, k2);
            
            ans.add(root.val);
            
            inorder(root.right, k1, k2);
        }
    }
    
    public ArrayList<Integer> searchRange(TreeNode root, int k1, int k2) {
        // write your code here
        inorder(root, k1, k2);
        
        return ans;
    }
}
