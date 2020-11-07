def permutation_palindrome(word):
    """
    For a word to have a permutation that is palindrome, every character in it should 
    have an even count except one (that is also not necessary, all chars can also have even counts)
    If one char has odd count, it can be at the center of the string to generate palindromes.
    NOTE: Ignore non-letter characters as they are not involved in checking palindrome
    Solution:
    Store the count of each char and check if at most one has an odd count
    """
    char_counts = {}
    for char in word:
        if not char.isalpha():
            # Ignore non-letter characters
            continue
        if char_counts.get(char) is None:
            char_counts[char] = 1
        else:
            char_counts[char] += 1

    # print(char_counts)

    # Check for odd counts
    odd_counts = 0
    for char, count in char_counts.items():
        # print(f'{char} || {count} || {odd_counts}')
        if count % 2 == 1:
            odd_counts += 1

    return odd_counts <= 1


if __name__ == '__main__':
    some_word = 'atco cta'
    print(permutation_palindrome(some_word.lower()))