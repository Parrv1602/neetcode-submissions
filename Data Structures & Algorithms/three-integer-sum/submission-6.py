class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            #If all numbers are positive, there are no numbers to cancel out and sum upto 0
            if nums[i] > 0: #Lowest number greater than 0
                break #Skip all loops
            
            #Duplicate numbers should be skipped because, if they are repeated, their same combinations of triplets will be appended to res
            if i and nums[i] == nums[i-1]:
                continue #Skip this iteration

            left = i + 1
            right = len(nums)-1
            while left < right:
                threeSum = nums[left] + nums[right] + nums[i]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    #Since this is appeneded, don't want to repeat future combinations with this number
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                
        return res