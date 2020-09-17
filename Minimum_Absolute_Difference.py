class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        res = []
        arr = sorted(arr)
        oldiff = 0
        for i in range(len(arr) - 1):
            a = arr[i]
            b = arr[i + 1]
            diff = abs(a - b)
            if i == 0:
                res.append([a, b])
                oldiff = diff
                continue
            if diff < oldiff:
                res = []
                res.append([a, b])
                oldiff = diff
            elif diff == oldiff:
                res.append([a, b])
                oldiff = diff
            else:
                continue
        return (res)
