class Solution {
public:
    // @param nestedList a list of NestedInteger
    // @return a list of integer
    vector<int> flatten(vector<NestedInteger> &nestedList) {
        // Write your code here
        using IT = vector<NestedInteger>::const_iterator;
        stack<pair<IT, IT>> depth_;
        vector<int> res;
        depth_.emplace(nestedList.cbegin(), nestedList.cend());
        while (!depth_.empty()) {
            auto &cur = depth_.top();
            if (cur.first == cur.second) {
                depth_.pop();
            } else if (cur.first->isInteger()) {
                res.push_back((depth_.top().first++)->getInteger());
            } else {
                auto &nestedList = cur.first->getList();
                ++cur.first;
                depth_.emplace(nestedList.cbegin(), nestedList.cend());
            }
        }
        return res;
    }
};
