class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            return 0

        if divisor == 1:
            return dividend
        if divisor * -1 == 1:
            return -1*dividend

        sign = 1
        if divisor < 0:
            sign = -1
            divisor = -1 * divisor

        if dividend < 0:
            sign *= -1
            dividend *= -1

        count = 0
        while dividend >= divisor:
            count += 1
            dividend -= divisor

        return count*sign
