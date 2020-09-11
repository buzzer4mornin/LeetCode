from collections import Counter

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        sums = 0
        mydict = Counter(S)
        print(mydict)
        for i in mydict.keys():
            if i in J:
                sums = sums + mydict.get(i)
        return sums