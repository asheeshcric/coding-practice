"""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false


Solution:
    dp array: Assign everything as False from [0:len(s)-1] and assign True to the end of string (making it the base case)
    1. We start from the end of the string and make our way to the beginning
    2. For any index i (from end:start), each word in the dictionary is compared with a substring i:i+len(word)
        - If the comparison is true, it means the word is present in the string. Then we check if another string is present from i+len(word) or not
        - So, we assign the same value at i, i.e. dp[i] = dp[i+len(word)]
    3. If we find True at dp[0], we are confirmed that words in the dictionary are present from each True location in the dp array
"""


def word_break(s, word_dict):
    dp = [False for _ in range(len(s) + 1)]
    dp[-1] = True
    for i in range(len(s) - 1, -1, -1):
        for word in word_dict:
            if i + len(word) <= len(s) and word == s[i : i + len(word)]:
                dp[i] = dp[i + len(word)]
            if dp[i]:
                break

    print(dp)
    return dp[0]


if __name__ == "__main__":
    s = "catsandog"
    word_dict = ["cats", "dog", "sand", "and", "cat"]
    print(word_break(s, word_dict))
