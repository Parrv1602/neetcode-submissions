class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       '''
        Logic: If the next price is greater than the current price, sell.
        If the current price is lesser than the next price, buy.

        But actually if the current number is greater than the previous number, it doesn't matter cause
        we can't buy on next day and sell on previous day (impossible).
       '''
       profit = 0
       for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])
        
       return profit
