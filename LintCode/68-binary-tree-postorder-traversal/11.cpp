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
    /**
     * @param root: The root of binary tree.
     * @return: Postorder in vector which contains node values.
     */
public:
    vector<int> postorderTraversal(TreeNode *root) {
        // write your code here
        vector<int> res;
        stack<TreeNode*> v;
        stack<TreeNode*> s;
        if(root){
            s.push(root);
            v.push(NULL);
        }
        
        while(!s.empty()){
            TreeNode *t = s.top();
            if(t == v.top()){
                s.pop();
                v.pop();
                res.push_back(t->val);
            }else{
                if(t->right){
                    s.push(t->right);
                }
                if(t->left){
                    s.push(t->left);
                }
                v.push(t);
            }
        }
        return res;
    }
};
