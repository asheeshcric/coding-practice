"""
You are given an array of strings products and a string searchWord.

Design a system that suggests at most three product names from products after each character of searchWord is typed. 
Suggested products should have common prefix with searchWord. 
If there are more than three products with a common prefix return the three lexicographically minimums products.

Return a list of lists of the suggested products after each character of searchWord is typed.
"""
from typing import List


"""
1. First, sort the products array in alphabetical order

2. For each prefix starting from index 0 all the way to the prefix word,
we keep track of the words that match the prefix using left and right pointers
in a sorted array
left: beginning product where the prefix matches
right: last product where the prefix matches
--> we only need the first three matched words: min(3, right-left+1)

3. If for a prefix, a product doesn't match at the any of the pointers,
we move it by one step: left += 1 or right -= 1

"""


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        # Sorting the names help us determine which results to show in the first three
        products.sort()
        left, right = 0, len(products) - 1
        result = []

        for i, char in enumerate(searchWord):
            matched_words = []
            while left <= right and (
                len(products[left]) <= i or products[left][i] != char
            ):
                # This means the product at left pointer does not match the prefix
                # Hence, does not need to be included in the search results
                left += 1

            while left <= right and (
                len(products[right]) <= i or products[right][i] != char
            ):
                right -= 1

            # Now that the left and right pointer are inclusive of all matched words,
            # we need to append first three words in the search list
            for k in range(min(3, right - left + 1)):
                matched_words.append(products[left + k])

            result.append(matched_words)

        return result
