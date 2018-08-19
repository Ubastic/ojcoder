class Solution {
public:
    string frequencySort(string s) {
        priority_queue<pair<int, char>> pq;
        unordered_map<char, int> char_count = countChar(s);
        for (const auto &p: char_count) {
            for (int i = 0; i != p.second; ++i) {
                pq.push(make_pair(p.second, p.first));
            }
        }
        string res;
        while (!pq.empty()) {
            auto p = pq.top();
            res += p.second;
            pq.pop();
        }
        return res;
    }
    
private:
    unordered_map<char, int> countChar(string &s) {
        unordered_map<char, int> res;
        for (const char c : s)  res[c]++;
        return res;
    }

};