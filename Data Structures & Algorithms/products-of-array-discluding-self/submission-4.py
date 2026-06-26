class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Create two lists: prefix and postfix.
        Prefix stores cumulatively multiplied values from index=0 to index=n


        '''
        result = [1] *len(nums)

        prefix = 1
        '''
        Initially store and THEN update prefix, otherwise the last value in the result list will be multiplied twice.
        The reason is also because we want to avoid multiplying the current number (the entire point of this problem).
        '''
        for i in range(len(nums)):
            #Multiply all numbers by the numbers before it
            result[i] = prefix
            prefix *= nums[i]
        
        '''
        What does the prefix represent? The cumulative multiplication of numbers. For example, the last element in prefix
        is cumulative multiplication of all numbers except for the last number.
        '''
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result
            
 