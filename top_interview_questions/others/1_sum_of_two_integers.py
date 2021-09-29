class Solution:

    """
    For any two positive integers x and y such that x >= y:
        a. sum_without_carry = x ^ y
        b. carry = (x & y) << 1

    Difference of x and y such that x >= y
        a. sum_without_borrow = x ^ y
        b. borrow = ((~x) & y) << 1

    """

    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)
        # ensure that abs(a) >= abs(b)
        if x < y:
            return self.getSum(b, a)

        # abs(a) >= abs(b) -->
        # a determines the sign
        sign = 1 if a > 0 else -1

        if a * b >= 0:
            # sum of two positive integers x + y
            # where x > y
            while y:
                answer = x ^ y
                carry = (x & y) << 1
                x, y = answer, carry
        else:
            # difference of two integers x - y
            # where x > y
            while y:
                answer = x ^ y
                borrow = ((~x) & y) << 1
                x, y = answer, borrow

        return x * sign
