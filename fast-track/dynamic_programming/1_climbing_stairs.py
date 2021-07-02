"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

def climb_stairs(n):
    dp = [None for _ in range(n+1)]
    return check_steps(n, dp)

def check_steps(n, dp):
    if n == 0:
        return 1
    if n < 0:
        return 0

    dp[n] = check_steps(n-1, dp) + check_steps(n-2, dp)
    return dp[n]

if __name__ == "__main__":
    print(climb_stairs(5))