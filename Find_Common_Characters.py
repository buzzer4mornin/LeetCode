from collections import Counter
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        hey=[]
        for j in A:
            hey.append(Counter(j))
        result =[]
        myword = hey[0]
        for i in myword:
            mino = myword.get(i)
            for word in hey[1:]:
                    if i not in word.keys():
                        mino = 0
                        break
                    mino = min(mino,word.get(i))
            if mino is not 0:
                for j in range(mino):
                    result.append(str(i))
        return result


print("Welcome to" , end = '2 ')
print("GeeksforGeeks", end = '3 ')
