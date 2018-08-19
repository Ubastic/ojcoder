class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def backtracking(ans, prev, left, right):
            if left == 0 and right == 0:
                ans.append(prev)
                return
            if left > 0:
                backtracking(ans, prev + "(", left - 1, right)
            if right > left:
                backtracking(ans, prev + ")", left, right - 1)
        backtracking(ans, "", n, n)
        return ans