def recursive_multiply(smaller, bigger):
    global dp
    if smaller == 0 or bigger == 0:
        return 0
    if smaller == 1:
        return bigger

    if dp[smaller][bigger] is not None:
        return dp[smaller][bigger]

    # Compute half of smaller
    half_smaller = smaller >> 1
    side1 = recursive_multiply(half_smaller, bigger)
    side2 = side1
    if smaller % 2 == 1:
        side2 = recursive_multiply(smaller-half_smaller, bigger)

    dp[smaller][bigger] = side1 + side2
    return dp[smaller][bigger]


num1 = 91
num2 = 82
bigger = num1 if num1 > num2 else num2
smaller = num1 if num1 < num2 else num2
dp = [[None for _ in range(bigger+1)] for _ in range(smaller+1)]
print(recursive_multiply(smaller, bigger))
