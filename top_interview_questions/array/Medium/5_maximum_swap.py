"""
1. First keep track of all the indices of the digits in the number
2. Loop through the digits and for each digit check whether:
    - Any number from 9 to (that_num - 1) is present after that or not
    - If yes, swap them and return

Note: Even if there are duplicate digits in the number, we store the index of the rightmost one as we always check to the right of any digit 
to see there exists a larger digit or not
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        digit_idx = {n: i for i, n in enumerate(str(num))}
        for k, digit in enumerate(str(num)):
            for nxt_digit in range(9, int(digit), -1):
                # Checking if there exists a larger digit after the current one
                if digit_idx.get(str(nxt_digit), -1) > k:
                    # Swap and return
                    result = [d for d in str(num)]
                    result[k], result[digit_idx[str(nxt_digit)]] = (
                        result[digit_idx[str(nxt_digit)]],
                        result[k],
                    )
                    return int("".join(result))

        return num
