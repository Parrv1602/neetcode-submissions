class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        Have to find max area of the container. Area = height (element array) * width (difference between indices)
        of the height elements.
        
        Use left and right pointers. Since we don't know the next area until we try it and the pointers
        would get closer to each other (width decreases), the maximum area can be found by using the height
        as the conditional.
        '''
        l,r = 0, len(heights) - 1
        area = 0
        max_area = 0
        while l < r:
            area = min(heights[l], heights[r])*(r-l)
            max_area = max(area, max_area)
            if heights[l] <= heights[r]:
                l += 1 #Move to greater height
            else:
                r -= 1
        
        return max_area

