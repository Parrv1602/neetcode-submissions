class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        frequency_map = defaultdict(int)

        for num in nums:
            frequency_map[num] += 1
        
        for i in range(len(nums)):
            frequency_map[nums[i]] -= 1 #To avoid reusing the same numbers 
            '''
            Skip code if two numbers are same because on the first iteration the correct triplet will be output,
            but on the second iteration the same duplicate number will be used and the same triplet will be formed,
            which violates the answers' rules.
            '''
            if i and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1, len(nums)):
                '''
                When finding a target, you don't want to accidentally get the current number again and 
                again and print out the same triplet. This is done to avoid adding the same numbers but
                in different order . For example, if the target is 5 and 5 exists in the dictionary, triplet is found,
                however on the second inner loop iteration, it may again ask, using the same numbers, if 5 exists, if it does
                then the same triplet it appended. So, decrease count to show that this number has already been "used".
                '''
                frequency_map[nums[j]] -= 1 
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j]) #Finding complement to make the sum 0
                if frequency_map[target] > 0:
                    res.append([nums[i], nums[j], target])

            #For next i, you want to have the numbers re-added, which are the numbers on the right.
            for j in range(i+1, len(nums)):
                frequency_map[nums[j]] += 1

        return res
        
