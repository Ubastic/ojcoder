class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        lst = []
        def dfs(lst, k):
            if k <= n:
                lst.append(k)
                p = 10 * k
                if p <= n:
                    for i in range(10):
                        dfs(lst, p + i)
                
        for i in range(1, 10):
            dfs(lst, i)
        return lst