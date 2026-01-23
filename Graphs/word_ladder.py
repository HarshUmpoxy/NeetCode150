# Word Ladder
# Solution: BFS

from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        queue = deque([(beginWord, 1)])  # (current_word, steps) the no. of steps will minimally be 1 even if source and dest are same

        # If beginWord is in the list, remove it to avoid revisiting
        if beginWord in word_set:
            word_set.remove(beginWord)

        while queue:
            word, step = queue.popleft()

            if word == endWord:
                return step

            for i in range(len(word)):
                original = word[i]
                for c in range(ord('a'), ord('z') + 1): # ord returns the Unicode (ASCII) integer value of a character
                    new_char = chr(c)
                    if new_char == original:
                        continue

                    new_word = word[:i] + new_char + word[i + 1:]
                    if new_word in word_set:
                        queue.append((new_word, step + 1))
                        word_set.remove(new_word)

        return 0
