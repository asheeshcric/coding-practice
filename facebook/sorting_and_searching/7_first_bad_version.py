def isBadVersion(version):
    return False


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        first_bad = 1
        while left <= right:
            mid = (left+right) // 2
            if isBadVersion(mid):
                # We know that there can be earlier bad versions too
                right = mid - 1
                first_bad = mid
            else:
                left = mid + 1

        return first_bad
