mydict = {"a": ".-",
          "b": "-...",
          "c": "-.-.",
          "d": "-..",
          "e": ".",
          "f": "..-.",
          "g": "--.",
          "h": "....",
          "i": "..",
          "j": ".---",
          "k": "-.-",
          "l": ".-..",
          "m": "--",
          "n": "-.",
          "o": "---",
          "p": ".--.",
          "q": "--.-",
          "r": ".-.",
          "s": "...",
          "t": "-",
          "u": "..-",
          "v": "...-",
          "w": ".--",
          "x": "-..-",
          "y": "-.--",
          "z": "--.."}


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        result = []
        for word in words:
            morseword = ""
            for i in word:
                morseword = morseword + mydict.get(i)
            if morseword not in result:
                result.append(morseword)
        return len(result)
