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
    int closestValue(TreeNode* root, double target) {
        int closest = root->val;
        TreeNode* node = root;
        while (node != NULL) {
            closest = abs(node->val - target) < abs(closest - target) ? node->val : closest;
            node = node->val > target ? node->left : node->right;
        }
        return closest;
    }
};