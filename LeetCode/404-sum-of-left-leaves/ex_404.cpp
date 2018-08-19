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
    int sumOfLeftLeaves(TreeNode* root) {
        int res = 0;
        if (root != NULL) {
            if (root->left != NULL && root->left->left == NULL && root->left->right == NULL) {
                res += root->left->val;
            }
            res += sumOfLeftLeaves(root->left) + sumOfLeftLeaves(root->right);
        }
        return res;
    }
};