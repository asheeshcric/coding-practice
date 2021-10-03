"""
So, we start with a number x that needs to be raised to the power of n

e.g: To evaluate 5 ^ 4,

we can do: (5^2)*(5^2)
or: (5^1)*(5^1)*(5^1)*(5^1)

Base cases:
if n == 0: return 1
if x == 0: return 0

result = self.recurse(x, n//2)
result = result * result
return result * x if n is odd else result
"""


class Solution:
    def recurse(self, x, n):
        if n == 0:
            return 1
        if x == 0:
            return 0

        result = self.recurse(x, n // 2)
        result = result * result
        return x * result if n % 2 == 1 else result

    def myPow(self, x: float, n: int) -> float:
        result = self.recurse(x, abs(n))
        return result if n >= 0 else 1 / result
