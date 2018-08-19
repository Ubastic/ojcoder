class Solution {
public:
    int countArrangement(int N) {
        vector<int> v;
        for (auto i = 0; i != N; ++i)
            v.push_back(i+1);
        return backtrack(v, N);
    }
    
private: 
    int backtrack(vector<int> &v, int n) {
        if (n <= 0) return 1;
        int count = 0;
        for (auto i = 0; i < n; ++i) {
            if (v[i] % n == 0 or n % v[i] == 0) {
                swap(v[i], v[n-1]);
                count += backtrack(v, n-1);
                swap(v[i], v[n-1]);
            }
        }
        return count;
    }
};