class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Set_nums = set(sorted(nums))
        longest = 0
        for num in Set_nums:
            if (num-1) not in Set_nums: #Means that this is the start of a sequence
                length = 0
                while (num+length) in Set_nums:
                    length += 1
                
                longest = max(length, longest)
        
        return longest
