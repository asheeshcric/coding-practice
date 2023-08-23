"""
You are given an array of variable pairs equations and an array of real numbers values, 
where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. 
Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. 
You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, 
so the answer cannot be determined for them.

"""
from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        self.create_graph(equations, values)

        # Now for each query (start, end), we need to do a dfs(start)
        # until we reach the end node

        results = []

        for start, end in queries:
            # For each equation, run a DFS to calculate the weights until you find the target
            ans = self.dfs(start, end)
            results.append(ans)

        return results

    def dfs(self, start, end):
        if start not in self.graph or end not in self.graph:
            return -1

        stack = [(start, 1)]
        visited = {start}
        while stack:
            node, result = stack.pop()
            if node == end:
                return result

            for neighbor, weight in self.graph[node]:
                if neighbor not in visited:
                    stack.append((neighbor, weight * result))
                    visited.add(neighbor)

        return -1

    def create_graph(self, equations, values):
        """
        First thing is to create a bidirectional graph with weights on their edges for each equation
        """

        self.graph = defaultdict(list)

        for i, var in enumerate(equations):
            var_x, var_y = var
            # Add neighbor as well as the values in both directions
            # e.g: if value for ["a", "b"] = 2, then a -> b = 2 and b -> a = 1/2
            self.graph[var_x].append((var_y, values[i]))
            self.graph[var_y].append((var_x, 1 / values[i]))
