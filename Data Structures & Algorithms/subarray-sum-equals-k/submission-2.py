class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefixSum = {0 : 1} #Initially 0 incase the first element = k
        for num in nums:
            curSum += num
            difference = curSum - k

            #Check if previous sub-arrays can be "subtracted" to get sub array that sums upto k.
            res += prefixSum.get(difference, 0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0) #Add any previous number of times that the curSum exists
        
        return res

