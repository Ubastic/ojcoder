public class Solution {
    public boolean repeatedSubstringPattern(String str) {
        return (str + str).substring(1, str.length() * 2 - 1).contains(str);
    }
}