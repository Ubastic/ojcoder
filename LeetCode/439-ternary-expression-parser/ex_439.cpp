class Solution {
public:
    string parseTernary(string expression) {
        if (expression.length() == 1)   return expression;
        int idx = findSplitIndex(expression);
        if (expression[0] == 'T')
            return parseTernary(expression.substr(2, idx - 2));
        else
            return parseTernary(expression.substr(idx + 1));
    }

private: 
    int findSplitIndex(string expression) {
        int count = -1, i = 2;
        while (i < expression.length()) {
            if (expression[i] == '?')
                count--;
            else if (expression[i] == ':') {
                count++;
                if (count == 0) break;
            }
            i++;
        }
        return i;
    }
};