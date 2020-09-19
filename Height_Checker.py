class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        mylist = sorted(heights)
        sums = 0
        for i in range(len(heights)):
            if mylist[i] != heights[i]:
                sums += 1
        return sums
