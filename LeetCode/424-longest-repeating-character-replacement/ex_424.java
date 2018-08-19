public class Solution {
    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int charCount = 0;
        int start = 0;
        int res = 0;
        int end = 0;
        while (end < s.length()) {
            count[s.charAt(end) - 'A']++;
            charCount = Math.max(charCount, count[s.charAt(end) - 'A']);
            end++;
            while (end - start - charCount > k) {
                count[s.charAt(start) - 'A']--;
                start++;
                for (int i : count) 
                    charCount = Math.max(charCount, i);
            }
            res = Math.max(res, end - start);
        }
        return res;
    }
}