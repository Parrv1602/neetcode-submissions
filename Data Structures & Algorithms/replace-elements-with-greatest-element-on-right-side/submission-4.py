class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result_array = [8]*len(arr)
        largest_right_value = -1
        '''
        Move backwards using the for loop.
        Why backwards? Because if you want to replace current element from elements that are greater from the right side
        start by searching from the right side instead of the left side. That way, you can immediately spot the largest element.
        '''
        for i in range(len(arr)-1,-1,-1):
            '''
            Because want to append -1 to the end and append the largest right value before finding the next right value
            which could/would be in the current iteration/ i.
            '''
            result_array[i] = largest_right_value
            largest_right_value = max(arr[i], largest_right_value)
        
        return result_array

