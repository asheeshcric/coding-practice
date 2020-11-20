class Solution:

    def count_sum(self, d, target):
        if d == 0:
            return (target == 0)

        if target == 0:
            return 1

        output = 0
        for i in range(1, self.max_face+1):
            if target-i >= 0:
                output = output + self.count_sum(d-1, target-i)

        return output

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d*f < target:
            return 0

        # Any die that can have this max face to contribute to the target
        if target == f and d > 1:
            self.max_face = f - (d-1)
        elif target > f:
            self.max_face = f
        else:
            self.max_face = target

        # Each dice has range (1, max_face) to choose from
        # Apply sum of n numbers = total algorithm
        return self.count_sum(d, target)
