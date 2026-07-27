class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        num_days = 0
        last_greatest_temp = 0
        #Use enumerate to loop through the index and the temperature at the same time
        for index, temp in enumerate(temperatures):
            #Reference to solution: The stack can store arrays as elements [temp, index of that temp]
            #Only check if the temperature is greater than the previous temperature
            while stack and temp > stack[-1][0]:
                #Pop, then append the num days until higher temperature found.
                #So, subtract the current index (index containing greater temperature) - index of that temperature to get num days 
                stack_temp, stack_index = stack.pop()
                res[stack_index] = index - stack_index #hottest day - day of previous temperature = days til new hottest day
            
            stack.append([temp, index])
        
        return res