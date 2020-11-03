def has_unique_chars(word):
    """
    1. Ask what kind of characters can be present in the string? ASCII or Unicode
        - Most probably, it is going to be ASCII (128 chars) or Extended ASCII (256 chars)
    2. Base case: If len(word) > 128 or 256, then it cannot have unique chars
    3. Store each char in the string to a dict and check if it already occured or not
    """
    if len(word) > 128:
        return False
    
    seen_chars = {}
    for char in word:
        if seen_chars.get(char):
            return False
        seen_chars[char] = True

    return True


if __name__ == '__main__':
    some_word = 'abcdefgh'
    print(has_unique_chars(some_word))