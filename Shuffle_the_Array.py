class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        nums1 = nums[0: int(len(nums)/2)]
        nums2 = nums[int(len(nums)/2): len(nums)]
        result = []
        for i in range(int(len(nums)/2)):
            result.append(nums1[i])
            result.append(nums2[i])
        return result


myobject = Solution()
test = myobject.shuffle([1, 2, 4, 6, 2, 4], 3)
print(test)