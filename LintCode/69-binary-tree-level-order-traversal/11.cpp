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
     * @return: Level order a list of lists of integer
     */
public:
    vector<vector<int>> levelOrder(TreeNode *root) {
        // write your code here
        queue<TreeNode*> q;
        vector<vector<int>> res;
        vector<int> level;
        if(!root)
            return res;
        
        q.push(root);
        q.push(NULL);
        
        while(q.size()){
            TreeNode* t = q.front();
            q.pop();
            if(t){
                level.push_back(t->val);
                if(t->left)
                    q.push(t->left);
                if(t->right)
                    q.push(t->right);
            }else{
                res.push_back(level);
                level.clear();
                if(q.size())
                    q.push(NULL);
            }
        }
        return res;
    }
};
