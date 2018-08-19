/*
@Copyright:LintCode
@Author:   ojcoder
@Problem:  http://www.lintcode.com/problem/binary-tree-serialization
@Language: C++
*/

class Solution {
public:
    /**
     * This method will be invoked first, you should design your own algorithm 
     * to serialize a binary tree which denote by a root node to a string which
     * can be easily deserialized by your own "deserialize" method later.
     */
    string serialize(TreeNode *root) {
        // write your code here
        ostringstream os;   
        serializeHelper(root, os);
        return os.str();
    }

    void serializeHelper(TreeNode *root, ostringstream &os){
        if(!root){
            os<<"# ";
            return;
        }else{
            os<<root->val<<" ";
            serializeHelper(root->left, os);
            serializeHelper(root->right, os);
        }
    }


    /**
     * This method will be invoked second, the argument data is what exactly
     * you serialized at method "serialize", that means the data is not given by
     * system, it's given by your own serialize method. So the format of data is
     * designed by yourself, and deserialize it here as you serialize it in 
     * "serialize" method.
     */
    TreeNode *deserialize(string data) {
        // write your code here
        TreeNode* root = NULL;   
        istringstream is;
        is.str(data);
        deserializeHelper(root, is);
        return root;
    }

    void deserializeHelper(TreeNode* &root, istringstream &is) {
        // write your code here
        while(is.peek() == ' ')
            is.ignore();
            
        if(is.peek() != '#'){
            int val;
            is>>val;
            root = new TreeNode(val);
            deserializeHelper(root->left, is);
            deserializeHelper(root->right,is);
        }else{
            root = NULL;
            is.ignore();
        }
    }
};
