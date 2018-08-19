class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        g = collections.defaultdict(lambda : collections.defaultdict(int))
        vset = set()
        for e, v in zip(equations, values):
            g[e[0]][e[1]] = v
            g[e[1]][e[0]] = 1.0 / v
            vset.add(e[0])
            vset.add(e[1])
        for v1 in vset:
            g[v1][v1] = 1.0
            for v2 in vset:
                for v3 in vset:
                    if g[v1][v2] and g[v2][v3]:
                        g[v1][v3] = g[v1][v2] * g[v2][v3]
        ans = []
        for i, j in queries:
            if g[i][j]:
                ans.append(g[i][j])
            else:
                ans.append(-1.0)
        return ans