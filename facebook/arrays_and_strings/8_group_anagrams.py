from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = dict()
        for s in strs:
            # Track count of all chars in each string (contains chars from a-z)
            count = [0] * 26
            for char in s:
                count[ord(char) - ord("a")] += 1
            
            if tuple(count) in result:
                result[tuple(count)].append(s)
            else:
                result[tuple(count)] = [s]

        return result.values()
