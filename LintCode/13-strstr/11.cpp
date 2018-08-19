/*
@Copyright:LintCode
@Author:   ojcoder
@Problem:  http://www.lintcode.com/problem/strstr
@Language: C++
*/

class Solution {
public:
    /**
     * Returns a index to the first occurrence of target in source,
     * or -1  if target is not part of source.
     * @param source string to be scanned.
     * @param target string containing the sequence of characters to match.
     */
    int strStr(const char *source, const char *target) {
        // write your code here
        if(source == NULL || target == NULL)
            return -1;
        if(target[0] == '\0')
            return 0;
        int start = 0;
        while( source[start] != '\0'){
            int t = 0;
            int s = 0;
            while(source[start+s] != '\0' && target[t] != '\0' && source[start+s] == target[t]){
                s++;
                t++;
            }
            if(target[t] == '\0')
                return start;
            start++;
        }
        return -1;
    }
};
