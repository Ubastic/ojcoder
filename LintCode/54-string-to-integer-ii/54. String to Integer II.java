public class Solution {
    /**
     * @param str: A string
     * @return An integer
     */
    public int atoi(String str) {
        // write your code here
        if(str == null || str.length() == 0) return 0;
        
        int index = 0, plus = 1, num = 0;
        char[] charS = str.toCharArray();
        
        while(index < charS.length && !(charS[index] == '+' || charS[index] == '-' || (charS[index] >= '0' && charS[index] <= '9'))) index++;
        
        if(index == charS.length) return num;
        
        if(charS[index] == '+') 
            index++;
        else if(charS[index] == '-'){
            plus = -1;
            index++;
        }
        
        while(index < charS.length && charS[index] >= '0' && charS[index] <= '9'){
            if(plus == 1 && (num > Integer.MAX_VALUE / 10 || (num == Integer.MAX_VALUE / 10 && charS[index] - '0' > Integer.MAX_VALUE % 10))) return Integer.MAX_VALUE;
            
            if(plus == -1 && (num < Integer.MIN_VALUE / 10 || (num == Integer.MIN_VALUE / 10 && '0' - charS[index] < Integer.MIN_VALUE % 10))) return Integer.MIN_VALUE;
            
            num = num*10 + plus*(charS[index++] - '0');
        }
        
        return num;
    }
}
