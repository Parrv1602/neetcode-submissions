class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #Create a dicitionary that stores the frequency of each integer
        dictionary = defaultdict(int)

        for num in nums:
            if num in dictionary.keys():
                dictionary[num] += 1
            else:
                dictionary[num] = 1
        
        largest_value = max(nums)
        smallest_value = min(nums)
        index = 0
        for val in range(smallest_value, largest_value+1):
            while dictionary[val] > 0:
                '''
                Loop through all the values from smallest to largest (skips values which aren't in
                the dictionary or nums array).
                A default dict eliminates key error incase there is no value for a certain number between
                smallest to largest. The loop will not execute
                '''
                nums[index] = val
                index += 1
                dictionary[val] -= 1
        
        return nums
            

