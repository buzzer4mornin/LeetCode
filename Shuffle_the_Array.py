class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        nums1 = nums[0: n]
        nums2 = nums[n: len(nums)]
        result = []
        for i in range(n):
            result.append(nums1[i])
            result.append(nums2[i])
        return result
