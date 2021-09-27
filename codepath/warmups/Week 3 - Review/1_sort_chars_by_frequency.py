class Solution:
    def frequencySort(self, s: str) -> str:
        freq = dict()
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        chars = list(freq.keys())
        chars.sort(key=lambda c: -freq[c])
        sorted_string = ""
        for char in chars:
            sorted_string += char * freq[char]

        return sorted_string
