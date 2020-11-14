def gen_counts(string):
    counts = {}
    for char in string:
        if counts.get(char) is None:
            counts[char] = 1
        else:
            counts[char] += 1

    return counts


def countCharacters(words, str):
    chars_counts = gen_counts(chars)
    len_sum = 0
    for word in words:
        word_counts = gen_counts(word)
        is_good = True
        for c, count in word_counts.items():
            if count > chars_counts.get(c, 0):
                is_good = False
                break
        if is_good:
            len_sum += len(word)

    return len_sum


if __name__ == '__main__':
    words = ["hello", "world", "leetcode"]
    chars = "welldonehoneyr"
    print(countCharacters(words, chars))
