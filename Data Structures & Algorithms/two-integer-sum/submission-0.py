class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        

        indice_target = []

        complement_dictionary = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in complement_dictionary.keys():
                indice_target.append(complement_dictionary[complement])
                indice_target.append(i)
            else:
                complement_dictionary[nums[i]] = i
        
        return indice_target

