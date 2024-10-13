from typing import *


class Trie:
    """
    A Trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store
    and retrieve keys in a dataset of strings, supporting operations like insert, search, and startsWith.
    Implement operations for a Trie class: initialize, insert, search, and startsWith.
    [MEDIUM] https://leetcode.com/problems/implement-trie-prefix-tree/
    """

    def __init__(self):
        self.childs: List[Optional[Trie]] = [None] * 26
        self.is_word: bool = False

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            i = ord(char) - ord("a")
            if node.childs[i] is None:
                node.childs[i] = Trie()
            node = node.childs[i]
        node.is_word = True

    def search(self, word: str, only_prefix=False) -> bool:
        node = self
        for char in word:
            i = ord(char) - ord("a")
            if node.childs[i] is None:
                return False
            node = node.childs[i]
        return node.is_word or only_prefix

    def starts_with(self, prefix: str) -> bool:
        return self.search(prefix, only_prefix=True)


class WordDictionary:
    """
    Design a data structure that supports adding new words and finding if a string matches any previously
    added string. The 'search' method can include dots ('.') where dots can be matched with any letter.
    Implement the WordDictionary class with methods 'addWord' and 'search'.
    [MEDIUM] https://leetcode.com/problems/design-add-and-search-words-data-structure/

    >>> wd = WordDictionary()
    >>> wd.add_word("at")
    >>> wd.add_word("and")
    >>> wd.add_word("an")
    >>> wd.add_word("add")
    >>> wd.search("a")
    False
    >>> wd.search(".at")
    False
    >>> wd.add_word("bat")
    >>> wd.search(".at")
    True
    """

    def __init__(self):
        self.childs: Dict[int, 'WordDictionary'] = {}
        self.is_word: bool = False

    def add_word(self, word: str) -> None:
        node = self
        for char in word:
            child = node.childs.get(ord(char), None)
            if child is None:
                child = WordDictionary()
                node.childs[ord(char)] = child
            node = child

        node.is_word = True

    def search(self, word: str, i=0) -> bool:
        if i == len(word):
            return self.is_word
        if word[i] == ".":
            return any(child.search(word, i + 1) for child in self.childs.values())

        child = self.childs.get(ord(word[i]), None)
        if child is None:
            return False
        return child.search(word, i + 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
