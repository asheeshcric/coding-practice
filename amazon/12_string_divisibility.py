s = 'bcdbcdbcd'
t = 'bcdbcd'

if t not in s:
    print(-1)
    exit()

def smallest_repeating(string):
    str_len = len(string)
    if str_len == 0 or str_len % 2 != 0:
        return string

    half_index = int(str_len/2)
    if string[:half_index] == string[half_index:]:
        return smallest_repeating(string[:half_index])
    else:
        return string

repeating_s = smallest_repeating(s)
repeating_t = smallest_repeating(t)

if repeating_s == repeating_t:
    print(repeating_s)
else:
    print(-1)