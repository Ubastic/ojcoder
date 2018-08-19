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
    TreeNode* convertBST(TreeNode* root) {
        sum = 0;
        return helper(root);
    }
private:
    int sum;
    TreeNode* helper(TreeNode* node) {
        if (node == NULL)   return NULL;
        helper(node->right);
        sum += node->val;
        node->val = sum;
        helper(node->left);
        return node;
    }
};