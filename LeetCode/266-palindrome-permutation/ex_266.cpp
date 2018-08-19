class Solution {
public:
    bool canPermutePalindrome(string s) {
        set<char> charSet;
        for (auto c : s) {
            if (charSet.find(c) != charSet.end())
                charSet.erase(c);
            else
                charSet.insert(c);
        }
        return charSet.size() < 2;
    }
};