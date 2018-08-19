/*
@Copyright:LintCode
@Author:   ojcoder
@Language: C++
*/

class Solution {
public:
    /*
     * @param a: The first integer
     * @param b: The second integer
     * @return: The sum of a and b
     */
    int aplusb(int a, int b) {
        // Just submit this code, then you will get accepted!
        int carry = 0;
        do{
            carry = a & b;
            b = a ^ b;
            a=carry<<1;
        }while(a);
        return b;
    }
};
