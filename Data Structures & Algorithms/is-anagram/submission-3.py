class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Anagram = same length and rearranged character form a different word
        '''
        if len(s)>len(t) or len(t)>len(s):
            return False

        s_list = []
        t_list = []

        #Index approach because want to go through characters of both words
        for i in range(len(s)):
           s_list.append(s[i])
           t_list.append(t[i])
        
        return sorted(s_list) == sorted(t_list)
