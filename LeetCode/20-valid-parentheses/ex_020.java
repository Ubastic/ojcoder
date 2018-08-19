public class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            switch (c) {
                case '(':
                case '[':
                case '{':   stack.push(c);  break;
                case ')':   if (stack.empty() || stack.peek() != '(')   return false; else stack.pop(); break;
                case ']':   if (stack.empty() || stack.peek() != '[')   return false; else stack.pop(); break;
                case '}':   if (stack.empty() || stack.peek() != '{')   return false; else stack.pop(); break;
                default:    break;
            }
        }
        return stack.empty();
    }
}