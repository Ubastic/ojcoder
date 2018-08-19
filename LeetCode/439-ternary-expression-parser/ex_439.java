public class Solution {
    public String parseTernary(String expression) {
        if (expression.length() == 1)   return expression;
        int idx = findSplitIndex(expression);
        if (expression.charAt(0) == 'T')
            return parseTernary(expression.substring(2, idx));
        else
            return parseTernary(expression.substring(idx + 1));
    }
    
    private int findSplitIndex(String exp) {
        int count = -1, i = 2;
        while (i < exp.length()) {
            if (exp.charAt(i) == '?')
                count--;
            else if (exp.charAt(i) == ':') {
                count++;
                if (count == 0) break;
            }
            i++;
        }
        return i;
    }
}