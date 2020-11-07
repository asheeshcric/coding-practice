def check_rotation(word1, word2):
    """
    Check if word1 and word2 are rotation of each other.
    if word1 = xy, then word2 should be yx for it to be a rotation of the word1
    Also, yx is a substring of xyxy, hence if we check if word2 is a substring of word1+word1,
    then we can say that it is a rotation of word1
    """
    return word2 in word1+word1


if __name__ == '__main__':
    word1 = 'waterbottle'
    word2 = 'erbottlewat'
    print(check_rotation(word1, word2))


