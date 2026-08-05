class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        nums_count = defaultdict(int)
        for num in nums:
            nums_count[num] += 1
        
        #Since array is sorted, skip duplicates because they would have the same triplet combinations
        for i in range(len(nums)):
            #If nums[i] already exists in nums_count dictionary, decrease num times it occurs to avoid reusing it
            nums_count[nums[i]] -= 1
            if i and nums[i] == nums[i-1]:
                continue
            
            #Once found a unique number
            for j in range(i+1, len(nums)): #Finding the second number
                #Avoid reusing the same number
                nums_count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j-1]: #Want to check numbers whilst going right, avoid checking same numbers checked using i index
                    continue
                
                #Once found a unique number
                target = -(nums[i] + nums[j])
                if nums_count[target] > 0:
                    res.append([nums[i], nums[j], target])
            
            #If you haven't found a triplet yet (or if nums_count is empty in the beginning)
            #Have to add back the num counts that were subtracted in earlier loops
            for j in range(i+1, len(nums)):
                nums_count[nums[j]] += 1
        
        return res

            
