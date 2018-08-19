class Solution {
public:
    vector<int> getModifiedArray(int length, vector<vector<int>>& updates) {
        vector<int> res(length, 0);
        for (auto &p : updates) {
            int start = p[0], end = p[1], val = p[2];
            res[start] += val;
            if (end + 1 < length)
                res[end + 1] -= val;
        }
        // for (int i = 1; i != length; ++i)
        //     res[i] += res[i - 1];
        partial_sum(res.begin(), res.end(), res.begin());
        return res;
    }
};