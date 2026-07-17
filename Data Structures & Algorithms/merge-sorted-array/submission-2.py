class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        Go backwards and add elements from nums2 into nums2 if greater than current nums1 element.
        If not, then "shift" the current element to the right (since n zeros are added to the right of the nums1 array).
        """
        last = m + n - 1

        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n-1] 
                n -= 1
            
            last -= 1
        
        #Can be that all nums from nums2 are not appended to nums1. The numbers which aren't are the smallest numbers,
        #so append them to the front.
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1

