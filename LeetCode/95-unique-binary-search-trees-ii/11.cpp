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
    vector<TreeNode *> generateTrees(int n) {
        if(n == 0)
            return vector<TreeNode *>();
        return generateTreesByRange(1, n);
    }
	// 1..n is the inorder traversal of BST,
	// pick each num i from 1~n as root, generate tree with range [1~i-1], [i+1~n]
    vector<TreeNode *> generateTreesByRange(int start, int end){
        vector<TreeNode *> res;
        if(start < 1 || end < 1 || start > end){
            res = { NULL };
            return res;
        }
        if(start == end){
            res = {new TreeNode(start)};
            return res;
        }
        vector<TreeNode *> leftTree, rightTree;
        for(int i = start; i <= end; i++){
            vector<TreeNode *> leftTrees = generateTreesByRange(start,i-1);
            vector<TreeNode *> rightTrees = generateTreesByRange(i+1, end);
            for(auto leftTree : leftTrees)
                for(auto rightTree : rightTrees){
                    TreeNode *root = new TreeNode(i);
                    root -> left = leftTree;
                    root -> right = rightTree;
                    res.push_back(root);
                }
        }
        return res;
    }  
};