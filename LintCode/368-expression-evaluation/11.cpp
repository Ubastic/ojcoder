class Solution {
public:
    /**
     * @param expression: a vector of strings;
     * @return: an integer
     */
    int evaluateExpression(vector<string> &expression) {
        // write your code here
        if(expression.empty())
            return 0;
        vector<string> str_post;
        postfix(str_post, expression);
        return compute(str_post);
    }
	//中缀表达式转换为后缀表达式
    int postfix(vector<string> &str_post, vector<string> &str_mid)
    {
        stack<string> opt;
        for(string n : str_mid)
        {
            if(n == "(")
                opt.push(n);
            else if(n == ")")
            {
                while(!opt.empty() && opt.top() != "(")
                {
                    str_post.push_back(opt.top());
                    opt.pop();
                }
                if(opt.empty())
                    return -1;
                if(opt.top() == "(")
                    opt.pop();
            }
            else if(n == "+" || n == "-" || n == "*" || n == "/")
            {
                int a1 = getRink(n);
                while(!opt.empty() && a1 <= getRink(opt.top()))
                {
                    str_post.push_back(opt.top());
                    opt.pop();
                }
                opt.push(n);
            }
            else
                str_post.push_back(n);
        }
        while(!opt.empty())
        {
            str_post.push_back(opt.top());
            opt.pop();
        }
        return 0;
    }
	//根据后缀表达式进行表达式求值
    int compute(vector<string> &tokens)
    {
        stack<int> res;
        for(string n : tokens)
        {
            if(n == "+")
            {
                int opt1 = res.top();res.pop();
                int opt2 = res.top();res.pop();
                res.push(opt2 + opt1);
            }
            else if(n == "-")
            {
                int opt1 = res.top();res.pop();
                int opt2 = res.top();res.pop();
                res.push(opt2 - opt1);
            }
            else if(n == "*")
            {
                int opt1 = res.top();res.pop();
                int opt2 = res.top();res.pop();
                res.push(opt2 * opt1);
            }
            else if(n == "/")
            {
                int opt1 = res.top();res.pop();
                int opt2 = res.top();res.pop();
                res.push(opt2 / opt1);
            }
            else
                res.push(stoi(n));
        }
        return res.top();
    }
	//获取运算符优先级
    int getRink(string &str)
    {
        if(str == "+" || str == "-")
            return 10;
        if(str == "*" || str == "/")
            return 20;
        if(str == "(")
            return 0;
        else 
            return -1;
    }
};