/*
@Copyright:LintCode
@Author:   ojcoder
@Problem:  http://www.lintcode.com/problem/binary-tree-serialization
@Language: Java
*/

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
class Solution {
    /**
     * This method will be invoked first, you should design your own algorithm 
     * to serialize a binary tree which denote by a root node to a string which
     * can be easily deserialized by your own "deserialize" method later.
     */
    private String getStr(TreeNode root, String str){
        if(root == null) return "";
        
        String left = getStr(root.left, str + "l"), right = getStr(root.right, str + "r");
        StringBuilder sb = new StringBuilder().append(str).append(" ").append(root.val);
        
        if(!left.isEmpty()) sb.insert(0, ",").insert(0, left);
        
        if(!right.isEmpty()) sb.append(",").append(right);
        
        return sb.toString();
    }
     
    public String serialize(TreeNode root) {
        // write your code here
        return getStr(root, "r");
    }
    
    /**
     * This method will be invoked second, the argument data is what exactly
     * you serialized at method "serialize", that means the data is not given by
     * system, it's given by your own serialize method. So the format of data is
     * designed by yourself, and deserialize it here as you serialize it in 
     * "serialize" method.
     */
    private TreeNode getNode(HashMap<String, Integer> M, String str){
        if(!M.containsKey(str)) return null;
        
        TreeNode root = new TreeNode(M.get(str));
        
        root.left = getNode(M, str + "l");
        
        root.right = getNode(M, str + "r");
        
        return root;
    }
    
    public TreeNode deserialize(String data) {
        if(data.isEmpty()) return null;
        
        // write your code here
        String[] strs = data.split(",");
        HashMap<String, Integer> M = new HashMap<>();
        
        for(String str : strs){
            String[] s = str.split(" ");
            
            M.put(s[0], Integer.parseInt(s[1]));
        }
        
        return getNode(M, "r");
    }
}
