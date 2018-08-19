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
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> res;
        helper(res, root);
        return res;
    }
private:
    void helper(vector<string> &res, TreeNode* root, string path = "") {
        if (!root)  return;
        path += to_string(root->val);
        if (!root->left && !root->right) {
            res.push_back(path);
            return;
        }
        path += "->";
        helper(res, root->left, path);
        helper(res, root->right, path);
    }
};