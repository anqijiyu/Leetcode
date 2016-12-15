class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        for x1, y1 in points:
            d = collections.defaultdict(int)
            for x2, y2 in points:
                d[(x2-x1)**2 + (y2-y1)**2] += 1
            for i in d:
                ans += d[i] * (d[i] - 1)
        return ans
