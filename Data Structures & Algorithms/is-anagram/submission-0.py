class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Anagram = same length and rearranged character form a different word
        '''
        s_dict = {}
        t_dict = {}
        if len(s)>len(t) or len(t)>len(s):
            return False

        #Index approach because want to go through characters of both words
        for i in range(len(s)):
            if s[i] not in s_dict.keys():
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] += 1
            
            if t[i] not in t_dict.keys():
                t_dict[t[i]] = 1
            else:
                t_dict[t[i]] += 1
        
        return s_dict == t_dict
