def sort_string(word):
    # Implement a sort function here...
    return sorted(word)


def update_char_count(char_counts, char):
    if char_counts.get(char) is None:
        char_counts[char] = 0
    else:
        char_counts[char] += 1

    return char_counts

def check_permutation(word1, word2):
    """
    Given two strings, check if one is a permutation of the other
    1. Ask if the comparison is case-sensitive or not?
    2. Ask if white space inside the string is significant or not?
    ----------------------------------------------------------------
    1. Base case: Two strings of different lengths cannot permutations of each other
    2. 1st option: Sort the words and compare
    3. 2nd option: Check char counts of both strings
    """
    # Base Case:
    if len(word1) != len(word2):
        return False

    # First option (Sorting string and comparing)
    # if sorted(word1) == sorted(word2):
    #     return True
    # else:
    #     return False

    # Second option (Count chars and compare)
    char_counts1 = dict()
    char_counts2 = dict()
    for i, char in enumerate(word1):
        char_counts1 = update_char_count(char_counts1, char)
        char_counts2 = update_char_count(char_counts2, word2[i])

    for char in char_counts1.keys():
        other_char = char_counts2.get(char)
        if char_counts1[char] != other_char:
            return False

    return True


if __name__ == '__main__':
    word1 = 'ashish'
    word2 = 'sshiah'
    print(check_permutation(word1, word2))
