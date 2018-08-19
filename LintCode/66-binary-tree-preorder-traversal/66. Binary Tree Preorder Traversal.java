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
     * @param root: The root of binary tree.
     * @return: Preorder in ArrayList which contains node values.
     */
    public ArrayList<Integer> preorderTraversal(TreeNode root) {
        // write your code here
        ArrayList<Integer> ans = new ArrayList<>();
        
        if(root == null) return ans;
        
        Stack<TreeNode> stk = new Stack<>();
        
        stk.push(root);
        
        while(!stk.isEmpty()){
            TreeNode node = stk.pop();
            
            while(node != null){
                ans.add(node.val);
                
                if(node.right != null) stk.push(node.right);
                
                node = node.left;
            }
        }
        
        return ans;
    }
}
