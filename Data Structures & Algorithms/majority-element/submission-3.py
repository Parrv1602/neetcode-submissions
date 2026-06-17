class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        import random
        '''
        My solution:
        dictionary = {}
        for num in nums:
            if num not in dictionary.keys():
                dictionary[num] = 1
            else:
                dictionary[num] += 1
        
        largest_num = 0
        highest_frequency = 0
        for num, frequency in dictionary.items():
            if frequency > highest_frequency:
                highest_frequency = frequency
                largest_num = num

        return largest_num
        '''

        #Optimised solution using random
        for i in range(len(nums)):
            random_num = random.choice(nums)
            if nums.count(random_num) > len(nums)//2:
                return random_num
