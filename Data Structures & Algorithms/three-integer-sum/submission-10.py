class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        dictionary = defaultdict(int)
        for num in nums:
            dictionary[num] += 1

        for i in range(len(nums)):
            dictionary[nums[i]] -= 1
        #Avoid same combination of numbers, ignore same number.
            if i and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)):
                dictionary[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j-1]:
                    continue
                
                #Find the difference between numbers, check if that complement existed.
                difference = -(nums[i] + nums[j])
                if dictionary[difference] > 0:
                    res.append([nums[i], nums[j], difference])
            
            for j in range(i+1, len(nums)):
                dictionary[nums[j]] += 1
            
        return res
