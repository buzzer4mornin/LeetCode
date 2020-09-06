a=1
b=-1
mydict = {"U":a,"D":b, "R":a,"L":b}
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        hor = 0
        ver = 0
        for i in moves:
            if i == "U" or i == "D":
                hor = hor + mydict.get(i)
            else:
                ver = ver + mydict.get(i)
        if ver == 0 and hor == 0:
            return True
