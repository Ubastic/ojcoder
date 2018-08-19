/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> findMode(TreeNode* root) {
        unordered_map<int, int> counter;
        vector<int> res;
        int mode_count = getModeCount(root, counter);
        for (auto &p : counter) {
            if (p.second == mode_count) {
                res.push_back(p.first);
            }
        }
        return res;
    }
    
private:
    int getModeCount(TreeNode *root, unordered_map<int, int>& counter) {
        if (root == NULL)   return 0;
        ++counter[root->val];
        return max(counter[root->val], max(getModeCount(root->left, counter), getModeCount(root->right, counter)));
    }
};