class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        tot = 0
        for list in grid:
            for i in range(len(list)):
                if list[i] >= 0:
                    continue
                tot = (len(list) - i)
                break
            result += tot
        return result
