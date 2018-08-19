class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        height_dict = {}
        height = []
        res = []
        for i in xrange(len(people)):
            p = people[i]
            if p[0] not in height_dict:
                height_dict[p[0]] = []
                height.append(p[0])
            height_dict[p[0]].append((p[1], i))
        height.sort(reverse=True)
        for h in height:
            height_dict[h].sort()
            for p in height_dict[h]:
                res.insert(p[0], people[p[1]])
        return res