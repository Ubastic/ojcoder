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
 * Example of iterate a tree:
 * BSTIterator iterator = new BSTIterator(root);
 * while (iterator.hasNext()) {
 *    TreeNode node = iterator.next();
 *    do something for node
 * } 
 */
public class BSTIterator {
    private Stack<TreeNode> stk = new Stack<>();
    //@param root: The root of binary tree.
    public BSTIterator(TreeNode root) {
        // write your code here
        TreeNode p = root;
        
        while(p != null){
            stk.push(p);
            p = p.left;
        }
    }

    //@return: True if there has next node, or false
    public boolean hasNext() {
        // write your code here
        if(!stk.isEmpty()) return true;
        
        else return false;
    }
    
    //@return: return next node
    public TreeNode next() {
        // write your code here
        TreeNode ans = stk.pop(), p = ans.right;
        
        while(p != null){
            stk.push(p);
            p = p.left;
        }
        
        return ans;
    }
}
