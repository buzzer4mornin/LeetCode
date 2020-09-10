class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sums = 0
        z = 1
        i = 0
        for row in mat:
                k = i - z
                sums = sums + row[i] + row[k]
                z += 2
                i += 1
        if len(mat[0])%2 != 0:
            sums = sums - mat[len(mat[0])/2][len(mat[0])/2]
        return sums
