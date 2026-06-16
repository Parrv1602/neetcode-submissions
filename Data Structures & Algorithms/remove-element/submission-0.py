class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        My interpretation:
            Eliminate all elements containing val, append those values in a list k, 
            then return k 
        '''
        k = 0
        '''
        k will increment only if nums[i] != val
        because we want to return only a list of nums with elements not equal to val
        So the dynamic updater, k, will replace values of the list nums with values that
        are not equal to k at the beginning of the array (incrementing from 0 onward.)
        '''
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k
        
        
