"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""
word1 = "pqrs"
word2 = "abc"

merged_string = ""
for i in range(min(len(word1), len(word2))):
    merged_string += word1[i] + word2[i]

merged_string += word1[i + 1 :] + word2[i + 1 :]

print(merged_string)
