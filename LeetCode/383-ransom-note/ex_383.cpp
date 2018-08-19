class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        map<char, int> dict;
        for (auto c : magazine) {
            if (dict.find(c) != dict.end())
                ++dict[c];
            else
                dict.emplace(c, 1);
        }
        for (auto c : ransomNote) {
            if (dict.find(c) != dict.end() && dict[c] > 0)
                --dict[c];
            else    
                return false;
        }
        return true;
    }
};