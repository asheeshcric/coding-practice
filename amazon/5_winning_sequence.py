# Inputs
lower_bound = 1
upper_bound = 4
n = 4

# Output: return the array (in strictly increasing first and strictly decreasing later) with max left side element
# Output: [11, 12, 11, 10]

def winning_sequence(n, lower_bound, upper_bound):
    diff = upper_bound - lower_bound

    # Case where array cannot be formed
    if n < 3 or diff*2+1 < n:
        return -1

    for i in range(1, n):
        if diff >= n-i-1 and diff >= i:
            break

    res = [-1]*n
    idx, upper = i, upper_bound
    while idx >= 0:
        res[idx] = upper
        idx -= 1
        upper -= 1

    idx, upper = i+1, upper_bound-1
    while idx < n:
        res[idx] = upper
        idx += 1
        upper -= 1

    return res

print(winning_sequence(n, lower_bound, upper_bound))