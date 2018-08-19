class Solution {
public:
    // @param nestedList a list of NestedInteger
    // @return a list of integer
    vector<int> flatten(vector<NestedInteger> &nestedList) {
        // Write your code here
        vector<int> result;
        for (const auto& node : nestedList)
            if (node.isInteger()) {
                result.push_back(node.getInteger());
            } else {
                vector<NestedInteger> sub_list = node.getList();
                auto temp = flatten(sub_list);
                result.insert(result.end(), temp.begin(), temp.end());
            }

        return result;
    }
};
