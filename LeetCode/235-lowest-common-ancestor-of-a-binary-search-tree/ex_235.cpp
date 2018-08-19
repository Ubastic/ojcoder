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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        auto small = p->val <= q->val ? p : q;
        auto large = q->val > p->val ? q : p;
        auto commonAncestor = root;
        while (commonAncestor->val < small->val || commonAncestor->val > large->val) {
            while (commonAncestor->val < small->val)
                commonAncestor = commonAncestor->right;
            while (commonAncestor->val > large->val)
                commonAncestor = commonAncestor->left;
        }
        return commonAncestor;
    }
};