class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_counter = 0
        word2_counter = 0
        if len(word1) <= len(word2):
            length = len(word1)-1
            flag = True
        else:
            length = len(word2)-1
            flag = False

        ret_str = ""
        while word1_counter <= length or word2_counter <= length:
            ret_str += word1[word1_counter]
            ret_str += word2[word2_counter]
            word1_counter += 1
            word2_counter += 1
        
        if flag:
            #word2 is longer than word1, then append rest of word2 to return string
            ret_str += word2[word2_counter:]
        else:
            ret_str += word1[word1_counter:]
        
        return ret_str
        
 