/*
@Copyright:LintCode
@Author:   wuxubj
@Problem:  http://www.lintcode.com/problem/invert-binary-tree
@Language: C++
@Datetime: 17-04-24 09:54
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
 #include<queue>
class Solution {
public:
    /**
     * @param root: a TreeNode, the root of the binary tree
     * @return: nothing
     */
    /* 递归实现
    void invertBinaryTree(TreeNode *root) {
        // write your code here
        if(root == NULL) return;
        TreeNode* temp;
        temp = root-> left;
        root->left = root -> right;
        root -> right = temp;
        invertBinaryTree(root->left);
        invertBinaryTree(root->right);
    }
    */
    /*迭代实现*/
    void invertBinaryTree(TreeNode *root){
        if(root == NULL) return;
        queue<TreeNode *> que;
        que.push(root);
        while(!que.empty())
        {
            TreeNode* pNode = que.front();
            que.pop();
            TreeNode *temp = pNode->left;
            pNode->left = pNode -> right;
            pNode->right = temp;
            
            if(pNode->left)
                que.push(pNode->left);
            if(pNode->right)
                que.push(pNode->right);
            
        }
    }
};