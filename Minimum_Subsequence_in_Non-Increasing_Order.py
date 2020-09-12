class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums, reverse=True)
        res = []
        while sum(res) <= sum(nums):
            res.append(nums[0])
            nums.remove(nums[0])
        return res
