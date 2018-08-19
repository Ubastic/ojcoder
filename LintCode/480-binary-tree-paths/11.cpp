/*
@Copyright:LintCode
@Author:   wuxubj
@Problem:  http://www.lintcode.com/problem/binary-tree-paths
@Language: C++
@Datetime: 17-04-24 08:59
*/

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
     * @param root the root of the binary tree
     * @return all root-to-leaf paths
     */
    vector<string> svec;
    vector<int> temp;
    void fun(vector<int> &ivec)
    {
        string str = "";
        for(vector<int>::size_type i = 0; i < ivec.size(); i++)
        {
            str+=to_string(ivec[i]);
            if(i != ivec.size() - 1)
                str+="->";
        }
        svec.push_back(str);  
    }
    vector<string> binaryTreePaths(TreeNode* root) {
        // Write your code here
        if(root == NULL) return svec;
        temp.push_back(root -> val);
        if(root -> left) binaryTreePaths(root -> left);
        if(root -> right) binaryTreePaths(root -> right);
        if(root -> left == NULL && root -> right == NULL)
            fun(temp);
        temp.pop_back();
        return svec;
    }
};