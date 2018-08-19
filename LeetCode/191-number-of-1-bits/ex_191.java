public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        n &= 0xFFFFFFFF;
        int count = 0;
        for (int i = 0; i < 32; i++) {
            count += 1 & n;
            n >>= 1;
        }
        return count;
    }
}