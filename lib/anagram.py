class Anagram: 

    def __init__(self, word):
        self.word = word


    # @property
    # def match(self):
    #     """The word property"""
    #     return self._word

    # @match.setter
    # def match(self, word, list):
    #     """Word must match list. Else return empty list"""
    #     if([letter for letter in word] == [letter for letter in list[0] or [letter for letter in list[1]]]):
    #         print("matches")
    #         self._word = word
    #     else:
    #         print("empty list")
    #         return []
    def match(self, words):
        print(self.word)
        # if([letter for letter in "word"] == [letter for letter in list[0] or [letter for letter in list[1]]]):
        #     print("matches")
        #     return
        # else:
        #     return []
        # for w in list:
        #     self.word.sort() == w.sort()

        sorted_word = "".join(sorted(list(self.word)))
        return [w for w in words if sorted_word == "".join(sorted(list(w)))]
        
        