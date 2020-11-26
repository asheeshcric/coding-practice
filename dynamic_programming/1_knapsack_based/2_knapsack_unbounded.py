def unboundedKnapsack(k, arr):
    # k = target sum
    # arr = array from which we need to take integers to find a sum that
    # does not exceed the target sum (k)
    if k == 0:
        return 0

    # Check if the number picked from arr is less than or equal to k
    sum = 0
    for item in arr:
        if item <= k:
            return max(unboundedKnapsack(k-item, arr),
                       unboundedKnapsack(k, arr))


if __name__ == '__main__':
    arr = [2, 3, 4]
    k = 10
    print(unboundedKnapsack(k, arr))
