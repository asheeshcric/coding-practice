from typing import List


class Solution:
    def create_adjacency(self, words):
        adj = {char: set() for word in words for char in word}

        # Now, we fill up the adj list for each unique char in the words list
        # We do that by comparing pairs of consecutive words in the list
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_len = min(len(word1), len(word2))
            # Check if the ordering is invalid when the second word is a prefix of the first
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                # Invalid ordering
                return ""

            # Now, compare each char in the words and add to the adj list when they don't match
            for j in range(min_len):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break

        return adj

    def alienOrder(self, words: List[str]) -> str:
        # First create an adjacency list to track the lexicographical order of the letters
        adj = self.create_adjacency(words)

        if adj == "":
            # Invalid ordering
            return ""

        # A dictionary to keep track of visited and visiting nodes/chars
        # False if completely visited, True if in the current visiting path, and Not present if not visited at all
        visited = dict()
        result = []

        def dfs(char):
            # This is a post order DFS, i.e. after we process all the neighbors, only then we add the current node
            # to the visited set

            if char in visited:
                # return False if already visited, True if it is in the current path <-- Detected a loop/cycle
                return visited[char]

            # Add this char to the visiting path
            visited[char] = True

            for neighbor in adj[char]:
                if dfs(neighbor):
                    # This means we encountered a loop, so we return True again
                    return True

            # If we did not encounter a loop, we assign the char as completely visited
            visited[char] = False

            # Add the char to the result
            result.append(char)

        # Now, for each char, we will run a DFS and if it does not detect a cycle, we return the result
        for char in adj.keys():
            if dfs(char):
                # Invalid relational order
                return ""

        # Since we did a post-order DFS, the result is stored in the reverse order
        result.reverse()
        return "".join(result)
