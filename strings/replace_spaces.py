def replace_spaces(word):
    """
    In case of multiple spaces, just replace them with one '%20'
    """
    space_indices = []
    for i, char in enumerate(word):
        if char == ' ':
            space_indices.append(i)
    
    last_index = 0
    new_string = ''
    for index in space_indices:
        if index != last_index: #Checks if there's a space already before this index
            new_string += word[last_index:index]
            new_string += '%20'
            
        last_index = index + 1

    return new_string

if __name__ == '__main__':
    some_string = 'some string is this  assad    '
    print(replace_spaces(some_string))