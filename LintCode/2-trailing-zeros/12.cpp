/*
@Copyright:LintCode
@Author:   ojcoder
@Language: C++
*/

class Solution {
 public:
    // param n : description of n
    // return: description of return 
    long long trailingZeros(long long n) {
        double x = 1;
        long long base = (long long)pow(5, x);
        long long res = 0;
        while(base <= n){
            res += n/base;
            base = (long long)pow(5, ++x);
        }
        return res;
    }
};
