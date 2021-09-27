from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        for word in strs:
            key = self.get_key(word)
            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())

    def get_key(self, word):
        key = [0] * 26
        for char in word:
            idx = ord(char) - ord("a")
            key[idx] += 1
        return tuple(key)
