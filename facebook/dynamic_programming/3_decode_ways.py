class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i):
            # Base cases
            if i in dp:
                # If solution is already present
                return dp[i]

            if s[i] == "0":
                # Bad case -- cannot be decoded
                return 0

            # Two ways to decode:

            # Can either take the single digit and move on to the next one
            result = dfs(i + 1)

            # OR, if the first digit is 1 or 2, we can take double digits too
            if i + 1 < len(s) and (
                s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")
            ):
                result += dfs(i + 2)

            dp[i] = result
            return result

        return dfs(0)
