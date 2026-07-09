class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        '''
        Find matching characters in s and t, as soon as a character is not matching, append
        the characters following the not-matching character to the end of string s and return the length
        of characters appended to s.
        '''
        s_list = list(s)
        t_list = list(t)
        
        t_list_index = 0
        s_list_index = 0

        print(s_list)
        print(t_list)
        while t_list_index < len(t_list) and s_list_index < len(s_list):
            if t_list[t_list_index] == s_list[s_list_index]:
                s_list_index += 1
                t_list_index +=1
            else:
                s_list_index += 1

        return len(t_list) - t_list_index
        
