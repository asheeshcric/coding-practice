"""
There are n cities. Some of them are connected, while some are not. 
If city a is connected directly with city b, and city b is connected directly with city c, 
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities 
and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 
if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""
from typing import List


class Solution:
    def dfs(self, node, isConnected):
        self.visited.add(node)
        for neighbor in range(len(isConnected)):
            if isConnected[node][neighbor] == 1 and neighbor not in self.visited:
                self.dfs(neighbor)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited = set()
        num_provinces = 0

        for node in range(len(isConnected)):
            if node not in self.visited:
                # Just count the number of connected components using DFS
                num_provinces += 1
                self.dfs(node, isConnected)

        return num_provinces
