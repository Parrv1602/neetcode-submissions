class Solution:
    def scoreOfString(self, s: str) -> int:
        
        score = 0
        char1_counter = 0
        char2_counter = 1
        char1_score = 0
        char2_score = 0

        while char2_counter < len(s):
            first_char_score = ord(s[char1_counter])
            adjucent_char_score = ord(s[char2_counter])
            print(first_char_score)
            print(adjucent_char_score)
            score += abs(first_char_score - adjucent_char_score)
            char1_counter += 1
            char2_counter += 1
        
        return score
