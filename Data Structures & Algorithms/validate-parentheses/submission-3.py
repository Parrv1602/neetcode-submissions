class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {")":"(", "]":"[", "}":"{"}

        '''
        Rule: The last open bracket must meet its corresponding close bracket immediately for the bracket to be valid.
        '''
        stack = []

        
        for bracket in s:
            if bracket in bracket_dict.values():
                    stack.append(bracket)
            else:
                #If empty input or input with one closing bracket, index out of range error will show up, so check stack condition first
                if stack and stack[-1] == bracket_dict[bracket]:
                        stack.pop()

                else:
                    return False
            
        
        return True if not stack else False
                

