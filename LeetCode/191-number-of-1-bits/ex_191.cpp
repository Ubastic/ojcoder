class Solution {
public:
    int hammingWeight(uint32_t n) {
        n &= 0xFFFFFFFF;
        int count = 0;
        for (int i = 0; i < 32; i++) {
            count += 1 & n;
            n >>= 1;
        }
        return count;
    }
};