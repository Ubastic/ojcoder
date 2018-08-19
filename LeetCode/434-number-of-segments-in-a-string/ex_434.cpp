class Solution {
public:
    int countSegments(string s) {
        stringstream ss;
        ss << s;
        ss.clear();
        int count = 0;
        while (ss >> s)
            ++count;
        return count;
    }
};