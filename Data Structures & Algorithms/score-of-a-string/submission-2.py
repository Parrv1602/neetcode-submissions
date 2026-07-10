class Solution:
    def scoreOfString(self, s: str) -> int:
        
        score = 0
        char1_counter = 0
        char2_counter = 1

        while char2_counter < len(s):
            score += abs(ord(s[char1_counter]) - ord(s[char2_counter]))
            char1_counter += 1
            char2_counter += 1
        
        return score
