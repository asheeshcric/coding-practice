"""
 1.     1
 2.     11
 3.     21
 4.     1211
 5.     111221 
 6.     312211
 7.     13112221
 8.     1113213211
 9.     31131211131221
10.     13211311123113112211
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            count = 1
            current = []
            for index in range(1, len(result)):
                if result[index] == result[index - 1]:
                    count += 1
                else:
                    current.append(str(count))
                    current.append(result[index - 1])
                    count = 1
            current.append(str(count))
            current.append(result[-1])
            result = "".join(current)
        return result
