class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        sum=0
        for i in range(len(points)-1):
            a = points[i]
            b = points[i+1]
            diff = max(abs(b[0]-a[0]), abs(b[1] - a[1]))
            sum = sum + diff
        print(sum)
        return int(sum)

