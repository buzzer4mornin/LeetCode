class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        res = []
        while sum(res) <= sum(nums):
                n = nums.pop()
                res.append(n)
        return res
        
