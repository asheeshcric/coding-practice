"""
Give a list of sorted distinct integers, find a magic index such that A[i] = i
Return False if no such index exists
"""


def get_magic_index(A):
    start, end = 0, len(A)-1
    while start <= end:
        mid = (start+end) // 2
        if A[mid] == mid:
            # This is the magic index
            return mid
        elif A[mid] > mid:
            # Lies in the left half
            end = mid-1
        else:
            start = mid+1

    return False


A = [-1, -2, 2, 2, 2, 20, 32]
print(get_magic_index(A))


# When elements are not distinct
def magic_index(A, start, end):
    if end < start:
        return False

    mid_index = (start+end) // 2
    mid_value = A[mid_index]

    if A[mid_index] == mid_index:
        return mid_index

    # Search Left
    left_index = min(mid_index-1, mid_value)
    left = magic_index(A, start, left_index)
    if left >= 0:
        return left

    # Search Right
    right_index = max(mid_index+1, mid_value)
    right = magic_index(A, right_index, end)

    return right


print(magic_index(A, 0, len(A)-1))
