class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #stores temperatures and indexes: element: [temperature, index]
        res=[0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                stack_temp, stack_index = stack.pop()
                res[stack_index] = i - stack_index
            
            stack.append([temp, i])
        
        return res
