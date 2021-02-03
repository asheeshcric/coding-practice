# The idea is to represent N as a sequence of length L+1 as:
# N = a + (a+1) + (a+2) + .. + (a+L)
# => N = (L+1)*a + (L*(L+1))/2
# => a = (N- L*(L+1)/2)/(L+1)
# We substitute the values of L starting from 1 till L*(L+1)/2 < N


def count_ways(N):
    count, L = 0, 1
    while L*(L+1) < 2*N:
        a = (N - (L*(L+1))/2) / (L+1)
        if a - int(a) == 0.0:
            count += 1
        L += 1
    return count


print(count_ways(21))