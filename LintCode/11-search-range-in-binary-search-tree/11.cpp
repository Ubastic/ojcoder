class Solution {
public:
    /**
     * @param root: The root of the binary search tree.
     * @param k1 and k2: range k1 to k2.
     * @return: Return all keys that k1<=key<=k2 in ascending order.
     */
    vector<int> searchRange(TreeNode* root, int k1, int k2) {
        // write your code here
        vector<int> res;
        stack<TreeNode*> stk;
        
        if(!root)
            return res;
                
        stk.push(root);
        while(!stk.empty()){
            TreeNode* t = stk.top();
            stk.pop();
            if(t){
                stk.push(t->right);
                stk.push(t);
                stk.push(t->left);
            }else if(!stk.empty()){
                t = stk.top();
                stk.pop();
                if(t){
                    if(t->val >=k1 && t->val <= k2){
                        res.push_back(t->val);
                    }else if(t->val > k2){
                        break;
                    }
                }
            }
        }
        return res;
    }
};
