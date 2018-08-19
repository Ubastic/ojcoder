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
     * @return: Postorder in ArrayList which contains node values.
     */
    public ArrayList<Integer> postorderTraversal(TreeNode root) {
        // write your code here
        ArrayList<Integer> ans = new ArrayList<>();
        
        if(root == null) return ans;
        
        Stack<TreeNode> stk = new Stack<>();
        HashSet<TreeNode> visited = new HashSet<>();
        
        stk.push(root);
        
        while(!stk.isEmpty()){
            TreeNode node = stk.pop();
            
            if(visited.contains(node)){
                ans.add(node.val);
            }else{
                visited.add(node);
                stk.push(node);
                if(node.right != null) stk.push(node.right);
                if(node.left != null) stk.push(node.left);
            }
        }
        
        return ans;
    }
}
