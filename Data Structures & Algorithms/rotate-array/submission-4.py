class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Since k can be larger than the array, remainder will give num positions to actually shift the elements
        k %= len(nums)

        def reverse_nums(l:int, r:int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1
        
        #First reverse array
        reverse_nums(0, len(nums) - 1)
        #Then reverse first part of the array (since it's still in order but on left side)
        reverse_nums(0, k - 1)
        #Then revere the right part of the array (since it's still in order but on the right side)
        reverse_nums(k, len(nums)-1)
