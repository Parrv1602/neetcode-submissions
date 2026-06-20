class Solution:
    def sortColors(self, nums: List[int]) -> None:
        dictionary = defaultdict(int)

        for num in nums:
            dictionary[num] += 1
        
        red = 0
        white = 1
        blue = 2

        index = 0
        for i in range(0,3):
            colour = i
            while dictionary[i] > 0:
                nums[index] = i
                index += 1
                dictionary[i] -= 1
    
        print(nums)
        