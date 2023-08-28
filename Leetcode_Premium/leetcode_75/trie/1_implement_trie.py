"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. 
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 
"""
from collections import defaultdict


class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            current = current.children[char]
            # Here, current.children[char] returns an empty TrieNode if char is not present
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            current = current.children.get(char)
            if not current:
                return False

        return current.is_end_of_word

    def startsWith(self, prefix):
        current = self.root
        for char in prefix:
            current = current.children.get(char)
            if not current:
                return False

        return True
