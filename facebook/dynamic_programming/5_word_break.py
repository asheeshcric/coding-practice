from typing import List


class Solution:
    """
    1. Start from the last char and start checking if any of the words in the dict matches the remaining substring or not
    2. If it matches, then the word break at that position is going to be True as a fact that dp[len(s)] is True
    3. This True value will crawl its way to dp[0] if all the words can be broken down properly
    
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        str_len = len(s)
        dp = [False] * (str_len + 1)
        dp[-1] = True

        for i in range(str_len - 1, -1, -1):
            for word in wordDict:
                # First check if there are enough chars in the substring to match the word
                if len(s) >= i + len(word) and s[i : i + len(word)] == word:
                    dp[i] = dp[i + len(word)]

                if dp[i]:
                    # If we've already matched a word at that index, we don't have to look further.
                    break

        # So, when we backtrack to the 0th index, if all the word breaks were found to be True, we'll have our result as True at dp[0]
        return dp[0]
