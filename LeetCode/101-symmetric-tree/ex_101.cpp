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
    bool isSymmetric(TreeNode* root) {
        return root == NULL || checkSymmetric(root->left, root->right);
    }
    
private:
    bool checkSymmetric(TreeNode* left, TreeNode* right) {
        if (left == NULL && right == NULL)  return true;
        if (left == NULL || right == NULL)  return false;
        return left->val == right ->val && checkSymmetric(left->left, right->right) && checkSymmetric(right->left, left->right);
    }
};