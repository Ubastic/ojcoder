class Solution {
public:
    int hammingDistance(int x, int y) {
        int diff = x ^ y;
        int distance = 0;
        while (diff > 0) {
            distance += diff & 1;
            diff >>= 1;
        }
        return distance;
    }
};