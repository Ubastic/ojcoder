class Solution {
public:
    /**
     * @param s : A string
     * @return : A string
     */
    string reverseWords(string s) {
        // write your code here
        string res;
        stack<char> stk;
        int sz = s.length();
        for(int i = sz -1; i>=0; i--){
            char c = s[i];
            if(c == ' '){
                if(!stk.empty()){
                    while(!stk.empty()){
                        res.push_back(stk.top());
                        stk.pop();
                    }
                    res.push_back(c);
                }
            }else{
                stk.push(c);
            }
        }
        while(!stk.empty()){
            if(stk.top()!= ' ')
                res.push_back(stk.top());
            stk.pop();
        }
        if(res.back() == ' ')
            res.pop_back();
        return res;
    }
};
