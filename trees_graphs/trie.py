class Node:

    def __init__(self):
        # Each node can have a max of 26 children (if we consider only lower-case chars)
        # print('Initializing Node')
        self.children = [None]*26
        self.is_word = False


class Trie:

    def __init__(self):
        # print('Initializing Trie')
        self.root = Node()

    def _char_to_index(self, char):
        # A helper function to return the index of a char (0-25)
        return ord(char) - ord('a')

    def insert(self, word):
        # Insert new word to the Trie
        current = self.root
        for char in word:
            index = self._char_to_index(char)
            if current.children[index] is None:
                current.children[index] = Node()
            current = current.children[index]

        current.is_word = True

    def search(self, word):
        # Search if a word or a substring is present in the Trie
        current = self.root
        for char in word:
            index = self._char_to_index(char)
            if current.children[index] is None:
                return False
            current = current.children[index]

        return True
