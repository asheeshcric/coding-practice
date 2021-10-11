from typing import List

"""
U: Given a list that runs in a circular fashion, find the next greater element for each element in the list
- e.g. [5, 4, 3, 2, 1] ==> [-1, 5, 5, 5, 5]
- e.g. [1, 2, 1] ==> [2, -1, 2]

- So, from the current number, if you traverse the array in a circular way, 
the first number that you find greater than the current one is the next number

e.g: For [5, 1, 3, 2, 1]
[-1, 3, 5, 5, 5]

M:
- Use a stack to store the indices of the next greater elements found so far
- Since this is a circular array, we repeat the same array twice to find the next greater element
- If stack is empty, we add current index to the stack
- Else: we check if top of the stack is smaller than the current index
    - If it is: We know that the next greater number of element at idx (top of the stack) is the current number
        - So, we add it to the result

- We use the stack just like the monotonic stack


"""


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1 for _ in range(n)]
        stack = []
        for i in range(n * 2):
            while stack and nums[stack[-1]] < nums[i % n]:
                result[stack.pop()] = nums[i % n]

            if i < n:
                stack.append(i)

        return result
