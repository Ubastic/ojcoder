public class Solution {
    public void reverseWords(char[] s) {
        reverse(s, 0, s.length);
        int r = 0;
        while (r < s.length) {
            int l = r;
            while (r < s.length && s[r] != ' ') r++;
            reverse(s, l, r);
            r++;
        }
    }
    
    private void reverse(char[] s, int l, int r) {
        --r;
        while (l < r) {
            char tmp = s[l];
            s[l++] = s[r];
            s[r--] = tmp;
        }
    }
}