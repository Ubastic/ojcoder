public class Solution {
    public int findComplement(int num) {
        int copy = num, i = 0;
        while (copy != 0) {
            copy >>= 1;
            num ^= (1 << i++);
        }
        return num;
    }
}