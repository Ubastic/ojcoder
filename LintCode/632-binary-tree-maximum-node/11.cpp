/*
@Copyright:LintCode
@Author:   wuxubj
@Problem:  http://www.lintcode.com/problem/binary-tree-maximum-node
@Language: C++
@Datetime: 17-04-24 08:29
*/

class Solution {
public:
    /**
     * @param root the root of binary tree
     * @return the max node
     */
    TreeNode* node = NULL;
	void preOrder(TreeNode* pRoot)
	{
		if (pRoot == NULL) return;
		//cout << pRoot->val << endl;
		if (pRoot->val > node->val)
			node = pRoot;

		preOrder(pRoot->left);
		preOrder(pRoot->right);
	}
	TreeNode* maxNode(TreeNode* pRoot) {
		// Write your code here
		if (pRoot == NULL) return node;
		node = pRoot;
		preOrder(pRoot);
		return node;
	}
};