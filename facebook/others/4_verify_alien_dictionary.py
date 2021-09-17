"""
Given a sequence of words written in the alien language, and the order of the alphabet,
return true if and only if the given words are sorted lexicographically in this alien language
"""
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        letterIndex = dict()
        for i, char in enumerate(order):
            letterIndex[char] = i

        for i, word1 in enumerate(words[:-1]):
            word2 = words[i+1]

            # Need to compare consecutive words and check their order
            for j in range(len(word1)):
                if j == len(word2):
                    # This means second word is a prefix of the first
                    return False

                if word1[j] != word2[j]:
                    if letterIndex[word2[j]] < letterIndex[word1[j]]:
                        return False
                    break

        return True
