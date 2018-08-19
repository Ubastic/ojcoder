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
    // Non-recursion
    void flatten(TreeNode *root){
        //write your code here
        if(root == NULL) return;
        TreeNode *cur = root;
        while(cur){
            if(cur -> left){
                TreeNode *temp = cur -> left;
                while(temp -> right) temp = temp -> right;
                temp -> right = cur -> right;
                cur -> right = cur -> left;
                cur -> left = NULL;
            }
            cur = cur -> right;
        }
    } 
};