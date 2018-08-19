class Solution {
public:
    vector<int> findPermutation(string s) {
        vector<int> res;
        int i = 1;
        for (char &c : s) {
            if (c == 'I') 
                for (int j = i, length = res.size(); j != length; --j)
                    res.push_back(j);
            ++i;
        }
        for (int j = i, length = res.size(); j != length; --j)
            res.push_back(j);
        return res;
    }
};