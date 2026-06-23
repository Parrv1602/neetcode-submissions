class Solution:
    def calPoints(self, operations: List[str]) -> int:
        '''
        Pop the last element, if it is "D" then pop the next element, add its double, then add the recently popped element.
        while loop because we need to update the indexes of the array incase if its double
        '''
        result_score = []
        total_score =  0

        for operation in operations:
            if operation == "D":
                result_score.append(int(result_score[-1])*2)
                total_score += result_score[-1]

            elif operation == "+":
                result_score.append(int(result_score[-1]) + int(result_score[-2]))
                total_score += result_score[-1]

            elif operation == "C":
                total_score -= result_score[-1]
                result_score.pop()

            else:
                result_score.append(int(operation))
                total_score += result_score[-1]

        return total_score
        