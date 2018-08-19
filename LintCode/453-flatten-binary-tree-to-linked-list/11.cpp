/*
@Copyright:LintCode
@Author:   ojcoder
@Problem:  http://www.lintcode.com/problem/flatten-binary-tree-to-linked-list
@Language: C++
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
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    // Recursion
    //reference:http://www.cnblogs.com/grandyang/p/4293853.html
    void flatten(TreeNode *root){
        //write your code here
        if(root == NULL)
            return;
        if(root->left) flatten(root->left);
        if(root->right) flatten(root->right);
        TreeNode* temp = root->right;
        root->right = root -> left;
        root -> left = NULL;
        while(root->right) root = root -> right;
        root -> right = temp;
    }
};