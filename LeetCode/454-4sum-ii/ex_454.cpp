class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        map<int, int> sum_map;
        int count = 0;
        for (auto &i : A) {
            for (auto &j :B) {
                ++sum_map[i + j];
            }
        }
        
        for (auto &i : C) {
            for (auto &j :D) {
                if (sum_map.find(-i - j) != sum_map.end()) {
                    count += sum_map[-i - j];
                }
            }
        }
        return count;
    }
};