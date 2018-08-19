/**
 * Definition of TreeNode:
 * class TreeNode {
 * public:
 *     int val;
 *     TreeNode *left, *right;
 *     TreeNode(int val) {
 *         this->val = val;
 *         this->left = this->right = NULL;
 *     }
 * }
 */

class Solution {
public:
    /**
     * @param root: The root of binary tree.
     * @return: Preorder in vector which contains node values.
     */
    vector<int> preorderTraversal(TreeNode *root) {
        // write your code here
        vector<int> res;
        stack<TreeNode*> stk;
        if(root)
            stk.push(root);
        while(!stk.empty()){
            TreeNode* t = stk.top();
            stk.pop();
            res.push_back(t->val);
            if(t->right)
                stk.push(t->right);
            if(t->left)
                stk.push(t->left);
        }
        return res;
    }
};
