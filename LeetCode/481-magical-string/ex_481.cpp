class Solution {
public:
    int magicalString(int n) {
        vector<int> s{1, 2, 2};
        int i = 2;
        while (s.size() < n) s.insert(s.end(), s[i++], 3 - s.back());
        return count(s.begin(), s.begin() + n, 1);
    }
};