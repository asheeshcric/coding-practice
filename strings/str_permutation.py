def permutation(str):
    e_permutation(str, '')


def e_permutation(str, prefix):
    if len(str) == 0:
        print(f'-----{prefix}------')
    else:
        for i in range(len(str)):
            rem = str[0:i] + str[i+1:]
            print(rem, prefix + str[i])
            e_permutation(rem, prefix+str[i])

permutation('cat')