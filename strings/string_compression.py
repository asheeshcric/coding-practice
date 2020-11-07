def compress(word):
    """
    For example, the string aabcccccaaa would become a2blc5a3
    """
    count = 1
    compressed_str = ''
    word_len = len(word)
    for i, char in enumerate(word):
        if word_len > i+1 and char == word[i+1]:
            count += 1
        else:
            compressed_str += char + str(count)
            count = 1
    return word if len(word) < len(compressed_str) else compressed_str
    

if __name__ == '__main__':
    word = 'aaaaaaabc'
    print(compress(word))