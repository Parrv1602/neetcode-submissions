class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        start_index, end_index = 0, len(s)-1
        while start_index < end_index:
            temp = s[start_index]
            s[start_index] = s[end_index]
            s[end_index] = temp
            start_index += 1
            end_index -= 1
            
