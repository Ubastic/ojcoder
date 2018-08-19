class Solution {
public:
    int characterReplacement(string s, int k) {
        vector<int> count(26);
        int charCount = 0;
        int start = 0;
        int res = 0;
        for (int end = 0; end != s.size(); ++end) {
            ++count[s[end] - 'A'];
            charCount = max(charCount, count[s[end] - 'A']);
            while (end - start - charCount + 1 > k) {
                count[s[start] - 'A']--;
                start++;
                for (int &i : count) 
                    charCount = max(charCount, i);
            }
            res = max(res, end - start + 1);
        }
        return res;
    }
};