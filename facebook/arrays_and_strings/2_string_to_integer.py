class Solution:
    def myAtoi(self, s: str) -> int:
        digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        # Remove all the whitespaces
        s = s.replace(" ", "")
        if not s:
            return 0

        # Check whether positive or negative
        sign = 1
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        result = ""
        for char in s:
            if char not in digits:
                break

            result += char

        if not result:
            return 0

        if type == 1:
            result = min(int(result), 2**31-1)
        else:
            result = min(int(result), 2**31)

        return result * sign
