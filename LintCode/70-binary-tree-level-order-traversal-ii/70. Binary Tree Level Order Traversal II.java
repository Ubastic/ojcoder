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
     * @return: buttom-up level order a list of lists of integer
     */
    public ArrayList<ArrayList<Integer>> levelOrderBottom(TreeNode root) {
        // write your code here
        ArrayList<ArrayList<Integer>> ans = new ArrayList<>();
        
        if(root == null) return ans;
        
        Queue<TreeNode> que = new LinkedList<>();
        
        que.offer(root);
        
        while(!que.isEmpty()){
            Queue<TreeNode> tmp = new LinkedList<>();
            ArrayList<Integer> l = new ArrayList<>();
            
            while(!que.isEmpty()){
                TreeNode node = que.poll();
                l.add(node.val);
                if(node.left != null) tmp.offer(node.left);
                if(node.right != null) tmp.offer(node.right);
            }
            
            ans.add(l);
            que = tmp;
        }
        
        Collections.reverse(ans);
        
        return ans;
    }
}
