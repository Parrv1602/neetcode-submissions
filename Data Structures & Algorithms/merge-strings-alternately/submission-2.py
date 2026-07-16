class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        counter = 0
        if len(word1) <= len(word2):
            length = len(word1)-1
            flag = True
        else:
            length = len(word2)-1
            flag = False

        ret_str = ""
        while counter <= length:
            ret_str += word1[counter]
            ret_str += word2[counter]
            counter += 1
        
        if flag:
            #word2 is longer than word1, then append rest of word2 to return string
            ret_str += word2[counter:]
        else:
            ret_str += word1[counter:]
        
        return ret_str
        
 