"""
There are n cities numbered from 0 to n - 1 and n - 1 roads such that 
there is only one way to travel between two different cities (this network form a tree). 
Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

Roads are represented by connections where connections[i] = [ai, bi] 
represents a road from city ai to city bi.

This year, there will be a big event in the capital (city 0), 
and many people want to travel to this city.

Your task consists of reorienting some roads such that each city can visit the city 0. 
Return the minimum number of edges changed.

It's guaranteed that each city can reach city 0 after reorder.

"""

from typing import List
from collections import deque


class Solution:
    """
    1. Start from city 0, check if the neighbors can reach 0
    2. Recursively, check the neighbors of the neighbors (BFS)
    3. At each level, count the number of edges that need to be flipped to connect the neighbors
    to city 0

    # Convert the connections into a set of edges for a constant lookup
    # Then create a bidirectional edge graph connecting the nodes

    """

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = {(a, b) for a, b in connections}
        graph = {city: [] for city in range(n)}
        for city_from, city_to in connections:
            # Irrespecity of the direction of the edge, we keep track of which nodes are connected
            # To help figure out the neighbors
            graph[city_from].append(city_to)
            graph[city_to].append(city_from)

        visited = set()
        reorder = 0
        # Since, we always start from city 0
        queue = deque([0])

        # BFS and check if neighbors of the current city are all connected to it or not
        while queue:
            city = queue.popleft()
            if city in visited:
                continue

            visited.add(city)
            for neighbor in graph[city]:
                if neighbor not in visited and (neighbor, city) not in edges:
                    # This means the neighbor is not connected to the city
                    reorder += 1

                queue.append(neighbor)

        return reorder


sol = Solution()
print(sol.minReorder(n=6, connections=[[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]))
