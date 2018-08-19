class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> res;
        for(string n : tokens)
        {
            if(n == "+" || n == "-" || n == "*" || n == "/")
            {
                int opt1 = res.top();
                res.pop();
                int opt2 = res.top();
                res.pop();
                if(n == "+")  res.push(opt2 + opt1);
                if(n == "-")  res.push(opt2 - opt1);
                if(n == "*")  res.push(opt2 * opt1);
                if(n == "/")  res.push(opt2 / opt1);
            }
            else
                res.push(stoi(n));
        }
        return res.top();
    }
};