class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')  #inf creates positive infinity
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
"""
example:
price = 7

min_price = min(∞, 7)
          = 7

max_profit = max(0, 7 - 7)
           = max(0, 0)
           = 0

"""