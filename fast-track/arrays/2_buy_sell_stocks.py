"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0
"""


def max_profit(prices):
    profit_max = 0
    min_price = float("inf")
    for price in prices:
        min_price = min(price, min_price)
        if price - min_price > profit_max:
            profit_max = price - min_price

    return profit_max


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(max_profit(prices))
