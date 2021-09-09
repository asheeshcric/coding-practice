class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Base case: If any of the nums is "0"
        if num1 == "0" or num2 == "0":
            return "0"

        # First create an array with all zeros that stores the result of the multiplication
        result = [0] * (len(num1) + len(num2))
        # Reverse both num1 and num2 to track their indices from the right such as ... 2, 1, 0
        num1, num2 = num1[::-1], num2[::-1]
        i1, i2 = 0, 0
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                output = int(num1[i1]) * int(num2[i2])
                # output will store the multplication result of the digits that we multiply
                # we need to store the mod to the index i1+i2 and dividend at the index i1+i2+1
                result[i1 + i2] += output
                result[i1 + i2 + 1] += result[i1 + i2] // 10
                result[i1 + i2] = result[i1 + i2] % 10

        # After the multiplication operation, the digits in result are stored in the reverse order
        # Also, it might contain some leading zeroes in case the length of the result is less than
        # len(num1) + len(num2). So, we will need to eliminate the leading zeros in case there are any

        # Reverse the digits to get to actual result
        result.reverse()

        # Remove all leading zeros
        begin = 0
        while result[begin] == 0:
            begin += 1

        result = result[begin:]
        # print(begin, result)
        return "".join([str(d) for d in result])
