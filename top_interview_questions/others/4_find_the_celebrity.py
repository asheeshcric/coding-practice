"""
U:
- There are n people in a party
    - One may be a celebrity who is known by everyone else
    - But the celebrity does not know any of them
    - There may not be any celebrity in the party

- Inp: "n" which is the number of people in the party
- Out: an integer between 0 to (n-1) representing the celebrity or -1 if there's no celebrity
- A helper function knows(a, b) is given that return True if a knows b

M:
- Keep track of people who do not know others in a hashset
"""


def knows(a: int, b: int) -> bool:
    # returns T or F based on the relation
    return True or False


class Solution:
    def findCelebrity(self, n: int) -> bool:
        candidate = 0
        for person in range(1, n):
            if knows(candidate, person):
                candidate = person

        # Now, we need to make sure that everyone knows the candidate and they don't know anyone
        for person in range(n):
            if person == candidate:
                continue
            if knows(candidate, person) or not knows(person, candidate):
                return -1

        return candidate
