class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        Pop elements from tokens. If an element is an opertor, then perform the arithmetic on the operands that
        were popped from tokens and place in another array.
        '''
        stack = [] 
        '''
        Since we are also performing operations on previous numbers that have been added, subtracted, etc, then
        you have to take the previous number appended from tokens and the previous previous number (which could've been
        either a plain number appended from tokens or a number which came from an arithmetic operation).
        This way there will only be at max two elements and, at the end of tokens, only 1 element in the stack which
        will be the final answer.
        '''

        for token in tokens:
            if token == "+": #Numbers already in the array. Assumed only two numbers in any arithmetic operation
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif token == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1)-int(num2))

            elif token == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))

            elif token == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1)/int(num2))

            else:
                stack.append(token)

        return int(stack[0])

