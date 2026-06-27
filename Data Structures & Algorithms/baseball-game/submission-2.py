class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        total_score = 0

        for operation in operations:
            if operation == "+":
                score.append(int(score[-1]) + int(score[-2]))
                total_score += int(score[-1])
            
            elif operation == "D":
                score.append(2*int(score[-1]))
                total_score += int(score[-1])
            
            elif operation == "C":
                total_score -= int(score[-1])
                score.pop()

            else:
                score.append(operation)
                total_score += int(score[-1])
        
        return total_score

