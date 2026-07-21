class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write_pointer = right = 0
        length = len(nums)

        while right < length:
            #Write unique elements in the front.
            nums[write_pointer] = nums[right]
            while right < length and nums[right] == nums[write_pointer]:
                right += 1
            
            write_pointer += 1 #Only write unique occurrences of an element at the front, ignore duplicates.
        
        return write_pointer
        
