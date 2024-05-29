#!/usr/bin/env python3

from typing import List

class Substring:
    def __init__(self):
        self.children = {}
        self.indexes = []

class SuffixTree:
    def __init__(self):
        self.root = Substring()

    def add(self, word: str, index: int):
        for i in range(len(word)):
            current = self.root
            for char in word[i:]:
                if char not in current.children:
                    current.children[char] = Substring()
                current = current.children[char]
                current.indexes.append(index)

    def search(self, substring: str) -> List[int]:
        current = self.root
        for char in substring:
            if char not in current.children:
                return []
            current = current.children[char]
        return current.indexes

class SSet:
    def __init__(self, fname: str) -> None:
        self.fname = fname
        self.tree = SuffixTree()
        self.words = []

    def load(self) -> None:
        with open(self.fname, 'r') as f:
            self.words = [line.rstrip() for line in f]
            for i in range(len(self.words)):
                self.tree.add(self.words[i], i)

    def search(self, substring: str) -> List[str]:
        indexes = self.tree.search(substring)
        return [self.words[i] for i in indexes]