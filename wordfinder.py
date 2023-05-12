"""Word Finder: finds random words from a dictionary."""


import random

class WordFinder:
    def __init__(self, path):
        self.words = self.read_words(path)
        print(f"{len(self.words)} words read")

    def read_words(self, path):
        with open(path, 'r') as f:
            return [word.strip() for word in f]

    def random(self):
        return random.choice(self.words)

wf = WordFinder('words.txt')
print(wf.random())
print(wf.random())
print(wf.random())
print(wf.random())

class SpecialWordFinder(WordFinder):
    def read_words(self, path):
        with open(path, 'r') as f:
            return [word.strip() for word in f if word.strip() and not word.startswith('#')]

swf = SpecialWordFinder('words.txt')
print(swf.random())
print(swf.random())
print(swf.random())
print(swf.random())
