from collections import Counter


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if len(moves) % 2 > 0:
            return False
        mydict = Counter(moves)
        if len(mydict) % 2 > 0:
            return False
        sum = 0
        b = False
        if "U" in mydict and "D" in mydict:
            sum = sum + int(mydict.get("U")) - int(mydict.get("D"))
            b = True
        if "R" in mydict and "L" in mydict:
            sum = sum + int(mydict.get("R")) - int(mydict.get("L"))
            b = True
        return sum == 0 and b == True

