class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {")":"(", "]":"[", "}":"{"}

        openingBracket_stack = []
        for bracket in s:
            if bracket in bracket_dict.values():
                openingBracket_stack.append(bracket)
            
            else:
                #Determine whether current closing bracket matches the opening bracket's corresponding closing bracket
                corresponding_opening_bracket = bracket_dict[bracket]

                if not openingBracket_stack or corresponding_opening_bracket != openingBracket_stack.pop():
                    return False
        
        return not openingBracket_stack
