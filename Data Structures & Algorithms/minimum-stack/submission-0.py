class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        #Compare val to recently smallest value appended to min stack. Smallest value stored on top
        #If values enterred are repeatedly larger, than the previous smaller value will continue to be appended
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)
            
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop() 

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
