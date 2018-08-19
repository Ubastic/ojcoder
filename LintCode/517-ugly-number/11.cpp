class Solution {
public:
    /**
     * @param num an integer
     * @return true if num is an ugly number or false
     */
    bool isUgly(int num) {
        // Write your code here
        if (num == 0)
            return false;
        int base = 2;
        while (num % base == 0)
            num /= base;
        base = 3;
        while (num % base == 0)
            num /= base;
        base = 5;
        while (num % base == 0)
            num /= base;
        return num == 1;
    }
};
