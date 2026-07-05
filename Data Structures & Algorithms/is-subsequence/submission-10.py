class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)

        counter_for_s = 0

        for i in range(len(t_list)):
            if counter_for_s == len(s_list):
                break
            elif s_list and s_list[counter_for_s] == t_list[i]: 
                counter_for_s += 1

        if len(s_list) == counter_for_s:
            return True
        else:
            return False