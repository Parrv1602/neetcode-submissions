class Solution:
    def guessNumber(self, n: int) -> int:
        '''
        -1 = higher
        1 = lower
        0 = number
        '''

        left, right = 1, n

        while left <= right:
            print("error")
            mid = (left+right)//2 #To get integer
            print("error 2")
            res = guess(mid)
            if res == 0:
                break
            elif res == 1:
                left = mid + 1
            else:
                right = mid - 1
        
        return mid
            
