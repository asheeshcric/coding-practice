from typing import List


class Solution:
    """
    To gain max profit, we have to buy a stock at the lowest possible price and sell it at the highest possible price after that
    i.e., the delta sell-buy should be maximum among all possible combinations

    The idea is to keep track of the least price for which you can buy the stock
    And moving further into the array, check if you can make a better profit than before if you can sell at the current price by checking the delta
    """

    def maxProfit(self, prices: List[int]) -> int:
        # Assume that we are buying at infinity and selling at -inf
        buy = float("inf")
        max_profit = 0
        for price in prices:
            buy = min(price, buy)
            max_profit = max(price - buy, max_profit)

        return max_profit
