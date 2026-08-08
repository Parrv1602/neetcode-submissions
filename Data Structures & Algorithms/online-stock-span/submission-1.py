class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            #Since we pop elements from the stack, we can't just +1 because number of elements decreases
            #And can't use counter to go backwards and increment span, that would be n square time complexity.
            span += self.stack[-1][1]
            self.stack.pop()

        self.stack.append([price, span])
        return span
        

        



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)