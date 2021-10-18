from typing import List

"""
U:
- Input: numCourses (labeled 0 to numCourses-1) and a list of prerequisites for different courses
- Output: return T/F based on if we can take all the courses or not satisfying all the prerequisites

- Build an adjacency list and this will be a directed graph
- Check if there's a cycle in the graph or not
    - If cycle is present, return False as we cannot complete all the courses

M:
- Graph DFS traversal with checking for a cycle

P:


"""


class Solution:
    def buildGraph(self, n, prerequisites):
        graph = {node: set() for node in range(n)}
        for course, prereq in prerequisites:
            graph[course].add(prereq)

        return graph

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        graph = self.buildGraph(numCourses, prerequisites)

        # If not present, hasn't been visited yet
        # elif visited[node] = False, is in the visiting state
        # else visited[node] = True, completely visited without finding any cycles
        visited = dict()

        def dfs(node):
            if node in visited:
                if visited[node] is False:
                    # This means we landed on a node that we're currently visiting: cycle found
                    return False
                else:
                    return True

            visited[node] = False

            for neighbor in graph[node]:
                if dfs(neighbor) is False:
                    return False

            visited[node] = True

            return True

        for node in graph:
            if node not in visited:
                if dfs(node) is False:
                    # Cycle found: cannot be finished
                    return False

        return True
