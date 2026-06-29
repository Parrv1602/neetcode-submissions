class MyStack:

    def __init__(self):
        #This is a double ended queue, where you can insert and delete elements at the front and back of the queue
       self.queue = deque()


    def push(self, x: int) -> None:
        self.queue.append(x)        


    def pop(self) -> int:
        '''
        To pop an element in a stack, the most recent element is removed, but in a double ended queue,
        the start pointer is at the beginning of the list and the end pointer is after the most recently 
        added element.

        So a solution is to remove the element at the beginning of the list and add it again at the end of the list.
        Continue to do this until the element that you want to pop is reached, then pop that element separately.

        This is achieved using leftpop()
        '''
        for i in range(len(self.queue)-1): #Don't pop the last element, else it will be re-added into the double ended queue
            self.queue.append(self.queue.popleft())

        return self.queue.popleft() #Pop the leftmost element which is the element needed to be popped


    def top(self) -> int:
        return self.queue[-1]


    def empty(self) -> bool:
        return len(self.queue) == 0

