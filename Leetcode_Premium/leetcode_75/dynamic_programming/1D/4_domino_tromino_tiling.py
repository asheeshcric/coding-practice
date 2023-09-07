"""
You have two types of tiles: a 2 x 1 domino shape and a tromino shape. 
You may rotate these shapes.


Given an integer n, return the number of ways to tile an 2 x n board. 
Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. 
Two tilings are different if and only if there are two 4-directionally adjacent cells on the board 
such that exactly one of the tilings has both squares occupied by a tile.



GET BACK TO THIS QUESTION TO UNDERSTAND IT FULLY....
"""


class Solution:
    def numTilings(self, n: int) -> int:
        prev, curr, tri = 1, 1, 0
        for i in range(1, n):
            #   n   prev  curr  tri
            #   1     1     1     0
            #   2     1     2     1
            #   3     2     5     2
            #   4     5    11     4
            prev, curr, tri = (
                curr,
                prev + curr + 2 * tri,
                prev + tri,
            )
        return curr % 1000000007
