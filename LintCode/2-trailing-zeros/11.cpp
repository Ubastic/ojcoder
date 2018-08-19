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
        long long res = 0;
        while(n){
            long long t = n/5;
            res+=t;
            n = t;
        }
        return res;
    }
};
