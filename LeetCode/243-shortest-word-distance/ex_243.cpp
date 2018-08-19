class Solution {
public:
    int shortestDistance(vector<string>& words, string word1, string word2) {
        int p1 = -1, p2 = -1, distance = INT_MAX;
        for (int i = 0; i != words.size(); ++i) {
            if (word1 == words[i]) p1 = i;
            if (word2 == words[i]) p2 = i;
            if (p1 != -1 && p2 != -1)
                distance = min(distance, abs(p1 - p2));
        }
        return distance;
    }
};