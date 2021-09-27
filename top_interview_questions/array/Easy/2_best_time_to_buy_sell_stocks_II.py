"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time.
However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

U:
- Input is a list of prices of a stock for several days. prices[i] ==> price of stock on ith day
- Return the max possible profit that can be made by buying and selling
- You can hold at most one share at a time. So, if you buy a stock, you will have to sell it before buying again

Cases:
1. What if a profit cannot be made? -- Do not buy it at all
2. Can buy and sell any number of times.

Ex: [1, 2, 3, 4, 5] ==> Buy on day 1 (price = 1) and sell on day 5 (price = 5) ==> profit = 5 - 1 = 4
Ex: [7,1,5,3,6,4] ==>
Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit = 4 + 3 = 7

Match ==> Traversing through the list and at each index try to find an upward trend
Plan:
1. Start from i=0, and start checking for upward trend
2. If upward_trend ==> keep going up until it reaches the peak and add that to the total_profit
3. Start from the next index to the peak and repeat until you reach the end of the list

I


R
E



"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        total_profit = 0
        while i < len(prices):
            profit, i = self.find_upward_trend(prices, i)
            total_profit += profit

        return total_profit

    def find_upward_trend(self, prices, i):
        # This function checks if there's an upward trend in the graph and if we can buy and sell
        # the stock to gain a profit
        profit = 0
        while i < len(prices) - 1:
            if prices[i] < prices[i + 1]:
                profit += prices[i + 1] - prices[i]
                i += 1
            else:
                return profit, i + 1

        return profit, i + 1
