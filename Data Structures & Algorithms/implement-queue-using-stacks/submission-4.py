class MyQueue:
    def __init__(self):
        '''
        The first stack will be used to pushing the elements.
        The second stack is used for popping the elements. Elements from the first stack will be popped and pushed
        onto the second stack. From there, if the second stack is not empty, then pop from that stack, else redo the
        process of pushing elements from the first stack.
        '''
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        return self.stack2[-1]

    def empty(self) -> bool:
        '''
        stack1 holds values pushed onto the stack.
        stack2 holds values popped from the stack.
        If either stack holds elements, then they aren't empty
        '''
        return max(len(self.stack1), len(self.stack2)) == 0
