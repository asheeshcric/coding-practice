big_string = 'kabcbasdacbhhgscba'
small_string = 'abc'


def get_char_counts(input_string):
    char_counts = dict()
    for char in input_string:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1

    return char_counts


def is_permutation(input_string, char_counts, len_small_string):
    temp_char_counts = dict(char_counts)
    total_sum = 0
    for char in input_string:
        if temp_char_counts.get(char):
            temp_char_counts[char] -= 1
            total_sum += 1

    return True if total_sum == len_small_string else False


def get_num_permutations(big_string, small_string):
    num_permutations = 0
    small_string_counts = get_char_counts(small_string)
    len_small_string = len(small_string)
    len_big_string = len(big_string)
    for idx in range(len_big_string):
        if idx+len_small_string > len_big_string:
            break

        if is_permutation(big_string[idx:idx+len_small_string], small_string_counts, len_small_string):
            print(big_string[idx:idx+len_small_string], small_string_counts)
            num_permutations += 1

    return num_permutations


print(get_num_permutations(big_string, small_string))

