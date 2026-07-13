class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        start_index, end_index = 0, len(s)-1
        while start_index < end_index:
            temp = s[start_index]
            s[start_index] = s[end_index]
            s[end_index] = temp
            start_index += 1
            end_index -= 1
            
'''
        while next_letter_i != len(s):
            if s[first_letter_i] < s[next_letter_i]:
                temp = s[first_letter_i]
                s[first_letter_i] = s[next_letter_i]
                s[next_letter_i] = temp
                first_letter_i += 1
                next_letter_i += 1 
            else:
                next_letter_i += 1

        return s
        '''