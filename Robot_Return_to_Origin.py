mydict = {"U":1,"D":-1, "R":1,"L":-1}
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        if(len(moves)%2>0):
            return false
        hor = 0
        ver = 0
        for i in moves:
            if i == "U" or i == "D":
                hor = hor + mydict.get(i)
            else:
                ver = ver + mydict.get(i)
        return ver == 0 and hor == 0
