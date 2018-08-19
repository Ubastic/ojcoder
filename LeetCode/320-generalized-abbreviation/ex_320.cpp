class Solution {
public:
    vector<string> generateAbbreviations(string word) {
        vector<string> res;
        helper(res, word, "", 0, true);
        return res;
    }
private:
    void helper(vector<string> &res, string word, string abbr, int i, bool use_number) {
        if (i == word.length()) {
            res.push_back(abbr);
            return;
        }
        helper(res, word, abbr + word[i], i + 1, true);
        if (use_number) {
            for (int j = 1; i + j <= word.length(); ++j) {
                helper(res, word, abbr + to_string(j), i + j, false);
            }
        }
    }
};