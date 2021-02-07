class Solution:

    def climbStairs(self, n: int) -> int:
        self.dp = [None] * (n+1)
        return self.num_ways(n)

    def num_ways(self, n):

        if n < 0:
            return 0

        if n == 0:
            return 1

        if self.dp[n] is not None:
            return self.dp[n]

        self.dp[n] = self.num_ways(n-1) + self.num_ways(n-2) + self.num_ways(n-3)

        return self.dp[n]


solution = Solution()
print(solution.climbStairs(9))
