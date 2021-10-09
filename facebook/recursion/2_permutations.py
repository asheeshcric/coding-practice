class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # Base case:
        if len(nums) == 1:
            return [nums[:]]

        result = []
        for i in range(len(nums)):
            n = nums.pop(0)
            permutations = self.permute(nums)

            for perm in permutations:
                perm.append(n)

            result.extend(permutations)
            nums.append(n)

        return result
