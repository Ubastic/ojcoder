/*
@Copyright:LintCode
@Author:   wuxubj
@Problem:  http://www.lintcode.com/problem/binary-tree-path-sum
@Language: C++
@Datetime: 17-04-24 07:07
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
     * @param root the root of binary tree
     * @param target an integer
     * @return all valid paths
     */
    vector<vector<int>> Ans;
	vector<int> temp;
	void Fun(vector<int> &iVec, int x)
	{
		int sum = 0;
		for (int i = 0; i < iVec.size(); i++)
			sum += iVec[i];
		if (sum == x)
			Ans.push_back(iVec);
	}

	vector<vector<int>> binaryTreePathSum(TreeNode* root, int target)
	{
		if (root == NULL)
			return Ans;
		temp.push_back(root->val);
		if (root->left) binaryTreePathSum(root->left, target);
		if (root->right) binaryTreePathSum(root->right, target);
		if (root->left == NULL && root->right == NULL)
			Fun(temp, target);
		temp.pop_back();
		return Ans;
	}
};