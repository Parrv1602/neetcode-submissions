class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        length = 0
        
        for i in range(len(s)-1, -1, -1):
            if ord(s[i]) != 32 and ord(s[i-1]) == 32:
                length +=1
                break
            elif ord(s[i]) != 32:
                length += 1
        
        return length

