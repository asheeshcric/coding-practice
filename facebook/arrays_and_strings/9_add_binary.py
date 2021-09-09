class Solution:
    def addBinary(self, a: str, b: str):
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        result = ""
        while i >= 0 or j >= 0:
            output = 0
            if i >= 0:
                output += int(a[i])
            if j >= 0:
                output += int(b[j])

            output += carry
            if output == 0:
                carry = 0
            elif output == 1:
                carry = 0
            elif output == 2:
                carry, output = 1, 0
            elif output == 3:
                carry, output = 1, 1

            result = str(output) + result
            i -= 1
            j -= 1
            
        if carry == 1:
            result = "1" + result

        return result
