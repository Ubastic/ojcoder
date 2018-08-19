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
    vector<vector<int>> findLeaves(TreeNode* root) {
        vector<vector<int>> res;
        height(res, root);
        return res;
    }
private:
    int height(vector<vector<int>> &res, TreeNode* root) {
        if (root == NULL)   return -1;
        int level = 1 + max(height(res, root->left), height(res, root->right));
        if (res.size() < level + 1)     res.push_back(vector<int>());
        res[level].push_back(root->val);
        return level;
    }
};