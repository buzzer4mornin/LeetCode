class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        new_arr = sorted(arr)
        return len({new_arr[i+1] - new_arr[i] for i in range(len(new_arr)-1)}) == 1
