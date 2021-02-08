"""
Given an input integer, find all possible combinations of valid paranthesis where the number of pairs is
equal to the input integer

"""


def gen_parenthesis(n, string, open_p, closed):
    global all_paranthesis
    if n == 0 and open_p == closed:
        all_paranthesis.append(string)

    if n >= 0:
        gen_parenthesis(n-1, string +
                        '(', open_p+1, closed)

        if open_p > closed:
            gen_parenthesis(n, string+')', open_p,
                            closed+1)

    return all_paranthesis


def parens(n):
    return gen_parenthesis(n, '', 0, 0)


all_paranthesis = []
print(parens(4))
