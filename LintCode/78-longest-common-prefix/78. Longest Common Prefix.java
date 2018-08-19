public class Solution {
    /**
     * @param strs: A list of strings
     * @return: The longest common prefix
     */
    public String longestCommonPrefix(String[] strs) {
        // write your code here
        if(strs == null || strs.length == 0) return "";
        
        String prefix = strs[0];
        
        for(int i = 1; i < strs.length; i++){
            int index = 0;
            
            while(index < prefix.length() && index < strs[i].length() && prefix.charAt(index) == strs[i].charAt(index)) index++;
            
            if(index == 0) return "";
            
            prefix = prefix.substring(0, index);
        }
        
        return prefix;
    }
}
