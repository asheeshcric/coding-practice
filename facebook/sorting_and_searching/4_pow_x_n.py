class Solution:
    def recurse(self, x, n):
        if n == 0:
            return 1
        if x == 0:
            return 0

        result = self.recurse(x, n//2)
        result = result * result
        return x * result if n % 2 == 1 else result

    def myPow(self, x: float, n: int) -> float:
        result = self.recurse(x, abs(n))
        return result if n >= 0 else 1 / result