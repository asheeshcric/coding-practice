"""
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...


AB = A * 26 ^1 + B *  26 ^ 0 = 1*26 + 2*1 = 28

It is similar to converting a hexadecimal number to decimal or binary to decimal

"""


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        mapping = dict()
        for i, ascii in enumerate(list(range(65, 65 + 26))):
            mapping[chr(ascii)] = i + 1

        number = 0
        for i, char in enumerate(columnTitle[::-1]):
            number += mapping[char] * (26 ** i)

        return number
