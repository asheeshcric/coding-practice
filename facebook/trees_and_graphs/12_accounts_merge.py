from typing import List


"""
1. First, create a graph (adjacency list) connecting all emails that are related to the same account
2. Second, keep track of the account name for each unique email
3. Find connected components in the graph:
    a. Each connected component refers to the same account.
    b. So, all unique emails in a connected component belong to the same account. Hence, sorting them gives the answer

    - Use DFS to traverse the graph and find the connected components

"""
from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        if not accounts:
            return []

        emailToName = dict()
        # The adj list will contain all emails connected to each email from all the accounts
        adj_list = defaultdict(set)
        visited = set()

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                first_email = account[1]
                adj_list[first_email].add(email)
                adj_list[email].add(first_email)
                emailToName[email] = name

        def dfs(email):
            visited.add(email)
            stack = [email]
            components = [email]
            while len(stack) > 0:
                email = stack.pop()
                for neighbor in adj_list[email]:
                    if neighbor in visited:
                        continue

                    # Add the neighbor to the stack
                    stack.append(neighbor)
                    components.append(neighbor)
                    visited.add(neighbor)

            return components

        # We need to run DFS from each email and see how many connected components are present
        result = []
        for email in adj_list:
            if email in visited:
                continue

            components = dfs(email)
            result.append([emailToName[email]] + sorted(components))

        return result
