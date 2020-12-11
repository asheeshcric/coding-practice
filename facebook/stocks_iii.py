def max_profit(A):
    n = len(A)
    if n < 2:
        return 0

    left = [0]*(n)
    right = [0]*(n)

    # First process the left array
    min_left = A[0]
    for i in range(1, len(left)):
        min_left = min(min_left, A[i])
        left[i] = max(left[i-1], A[i]-min_left)

    # Similarly, do it for right array
    max_right = A[n-1]
    for i in range(len(right)-2, -1, -1):
        max_right = max(max_right, A[i])
        right[i] = max(right[i+1], max_right-A[i])

    max_prof = 0
    for i in range(0, n-1):
        max_prof = max(max_prof, left[i]+right[i])

    return max_prof
