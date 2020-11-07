def one_replace(word, edit):
    replaced = False
    for i, char in enumerate(word):
        if char != edit[i]:
            if replaced:
                return False
            replaced = True
    return True


def one_insert(word, edit):
    inc = 0
    for i, char in enumerate(word):
        if char != word[i+inc]:
            inc += 1
            if inc > 1:
                return False

    return True


def is_one_away(word, edit):
    """
    An edit can be: insertion, deletion or replacement
    Check if a string is one edit away to become the edited string
    e.g.: pale is one away from ple (a is deleted)
    Solution: Check for three conditions separately with the help of the lengths of the strings
    """
    len1, len2 = len(word), len(edit)
    if len1 == len2:
        return one_replace(word, edit)
    elif len1+1 == len2:
        return one_insert(word, edit)
    elif len1-1 == len2:
        # Opposite of insertion
        return one_insert(edit, word)
    else:
        return False


if __name__ == '__main__':
    word = 'palen'
    edit = 'pale'
    print(is_one_away(word, edit))