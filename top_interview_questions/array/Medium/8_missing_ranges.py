"""
You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b


U:
    Inp: An inclusive range [lower, upper] and a list of nums within that range
    Out: A list of ranges that do not conver any number in the given list

    Input: nums = [0,1,3,50,75], lower = 0, upper = 99
    Output: ["2","4->49","51->74","76->99"]
    Explanation: The ranges are:
    [2,2] --> "2"
    [4,49] --> "4->49"
    [51,74] --> "51->74"
    [76,99] --> "76->99"

    - Base Cases:
        1. If nums = [], return ["lower->upper"]
        2. If in any range in the output left == right, just add the left value: ["-2->1", "2", "5->7"]
        3. If no missing ranges, return []


M: 
- Initially, before traversing through the numbers in the list, we assume that the whole range is missing
    - output = [(lower, upper)]

- new_range = True
  for each number in the list:
    if new_range:
        output.append((num, num))
        new_range = False
    else:
        last_range = output[-1]
        if last_range[1] == num + 1:
            # This means we need to expand the range by 1
            output[-1] = (last_range[0], last_range[1]+1)
        else:
            # We need to start a new range
            output.append((num, num))
            new_range = True

- After you get all ranges for the numbers in the list, we need to deduce the missing ranges
- Start from lower and the first item in the output
    - Check if first[0] > lower:
        - then result.append((lower, first-1))
        lower = first[1] + 1


"""
from typing import List

"""
Explanation: 
[1, 2, 5, 10, 12], lower=-1, upper=15

Step 1: prev = -2, curr = 1
 check the range (-1, 0) is valid or not, i.e. -1 < 0:
    - if valid, add it to the result
    - prev = curr = 1

Step 2: prev=1, curr=2, (2, 1) <== invalid range (does not get added)
Step 3: prev=2, curr=5 ==> (3, 4) <== valid range (added)
Step 4: prev=5, curr=10 ==> (6, 9) (added)
Step 5: prev=10, curr=12 ==> (11, 11) (added)
Step 6: prev=12, curr=16 (upper+1) ==> (13, 15) (added)
 
"""


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[int]:
        prev = lower - 1
        result = []
        for i in range(len(nums) + 1):
            current = nums[i] if i < len(nums) else upper + 1
            if prev + 1 <= current - 1:
                # Checking if the range is valid and missing from the list
                result.append(self.format_range(prev + 1, current - 1))

            prev = current

        return result

    def format_range(self, left, right):
        if left == right:
            return str(left)
        else:
            return f"{left}->{right}"
