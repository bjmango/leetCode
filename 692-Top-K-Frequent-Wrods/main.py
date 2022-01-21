import collections
from typing import List


def topKFrequent(words: List[str], k: int) -> List[str]:
    counter = collections.Counter(words)
    result = sorted(counter, key=lambda word: (-counter[word], word))
    return result[:k]


assert topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2) == ["i", "love"]
assert topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3) == ["i", "love", "coding"]
assert topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4) == ["the", "is", "sunny", "day"]
