"""
Find all permutations of a string without any duplicate characters

1. Loop through each char in the string
2. For each char, find all permutations using the same recursive function (loop through it)
3. Add the char and the permutation at each iteration to the main list
4. Return the list or ['']
"""


def permute(string):
    return [char + permutation for i, char in enumerate(string)
            for permutation in permute(string[:i] + string[i+1:])] or ['']


def permute_simple(string):
    permutations = set()
    for i, char in enumerate(string):
        for permutation in permute(string[:i]+string[i+1:]):
            permutations.add(char + permutation)

    return permutations or ['']


print(permute_simple('abca'))
