class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)):
            curr_num = arr[i]
            highest = 0
            for j in range(i+1, len(arr)):
                if arr[j] > highest:
                    highest = arr[j]
            
            arr[i] = highest

        arr[-1]=-1
        return arr