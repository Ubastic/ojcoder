public class Solution {
    /**
     * @param source: A string
     * @param target: A string
     * @return: A string denote the minimum window
     *          Return "" if there is no such a string
     */
    public String minWindow(String source, String target) {
        // write your code
        if(source == null || target == null || source.length() == 0 || target.length() == 0) return "";
        
        char[] sChar = source.toCharArray();
        HashMap<Character, Integer> cToNum = new HashMap<>(), tmp = new HashMap<>();
        int minLen = Integer.MAX_VALUE, minStart = 0, minEnd = 0, count = 0;
        
        for(char c : target.toCharArray()) cToNum.put(c, (cToNum.containsKey(c) ? cToNum.get(c) : 0) + 1);
        
        for(int start = 0, end = 0; end < sChar.length; end++){
            if(!cToNum.containsKey(sChar[end])) continue;
            
            tmp.put(sChar[end], (tmp.containsKey(sChar[end]) ? tmp.get(sChar[end]) : 0) + 1);
            
            if(tmp.get(sChar[end]) <= cToNum.get(sChar[end])) count++;
            
            if(count == target.length()){
                while(!cToNum.containsKey(sChar[start]) || cToNum.get(sChar[start]) < tmp.get(sChar[start])){
                    if(cToNum.containsKey(sChar[start]) && cToNum.get(sChar[start]) < tmp.get(sChar[start])) tmp.put(sChar[start], tmp.get(sChar[start]) - 1);
                    
                    start++;
                }
                
                int len = end - start + 1;
                
                if(len < minLen){
                    minLen = len;
                    minStart = start;
                    minEnd = end;
                }
            }
        }
        
        return count == target.length() ? source.substring(minStart, minEnd + 1) : "";
    }
}
