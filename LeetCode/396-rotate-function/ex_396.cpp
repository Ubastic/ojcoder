class Solution {
public:
    int maxRotateFunction(vector<int>& A) {
        int value = 0;
        size_t sz = A.size();
        for (auto i = 0; i != sz; ++i) {
            value += i * A[i];
        }
        int sumA = accumulate(A.cbegin(), A.cend(), 0);
        int max_value = value;
        for (auto i = 0; i != sz; ++i) {
            value += sumA - sz * A[sz - i - 1];
            max_value = max(value, max_value);
        }
        return max_value;
    }
};