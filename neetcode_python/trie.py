from typing import *


class Trie:
    def __init__(self):
        self.childs = [None] * 26
        self.is_word = False

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
        if only_prefix:
            return True
        return node.is_word

    def starts_with(self, prefix: str) -> bool:
        return self.search(prefix, only_prefix=True)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
