class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        dict_array = defaultdict(int)

        for i in range(len(nums)):
            dict_array[nums[i]] += 1
        
        max_val = max(nums)
        min_val = min(nums)

        #Now we will append the values from default dict to the nums array using two pointers
        counter = 0
        for value in range(min_val, max_val+1): #Python's range() excludes last number in loop
            #We will decrement the frequency of a number in the default dict when appending that value in
            #the nums array (values are replaced in the nums array).
            while dict_array[value] > 0:
                nums[counter] = value
                counter += 1
                dict_array[value] -= 1
        
        return nums

