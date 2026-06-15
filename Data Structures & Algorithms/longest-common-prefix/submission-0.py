class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        prefix = ""

        #To keep similar words/ word that is contained within another word together
        sorted_words = sorted(strs)
        word1 = sorted_words[0]
        #Ensure that word contained within another word and the other word are not chosen
        word2 = sorted_words[-1]
        
        if len(word1) >= len(word2):
            length = len(word2)
        else:
            length = len(word1)

        
        for i in range(length):
            if word1[i] != word2[i]:
                return prefix
            prefix += word1[i]
                
        return prefix

