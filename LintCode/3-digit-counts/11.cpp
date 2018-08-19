/*
@Copyright:LintCode
@Author:   ojcoder
@Language: C++
*/

class Solution {
public:
    /*
     * param k : As description.
     * param n : As description.
     * return: How many k's between 0 and n.
     */
    int digitCounts(int k, int n) {
        int res = 0;
        int base = 1;
        while (base <= n){
            // caculate how many k's <(n/(base*10))*(base*10) at pos base
            int a = n/(base*10);
            if (base>1 && k==0 && a>0)
                a--;
            a*=base;

            //caculate how many k's >=(n/(base*10))*(base*10) at pos base
            int digit = (n/base)%10;
            int b = 0;
            if (k<digit)
                b = base;
            else if (k==digit)
                b = n%base + 1;
            if (k==0 && n<base*10)
                b = 0;

            res+=(a+b);
            base*=10;
        }
        return res;    
    }
};
