class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        length = 0
        char_counter = len(s)-1

        while s[char_counter] == " ":
            char_counter -= 1
   
        while char_counter>=0 and s[char_counter] != " ": 
            length += 1
            char_counter -= 1
        
        return length
