from collections import Counter

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mydict = Counter(nums)
        print(mydict)
        ssum = 0
        for i in mydict.values():
            if i==1:
                continue
            ssum = ssum + sum(range(i))
        return ssum
