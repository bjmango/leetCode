from typing import List


def wordBreak(s: str, wordDict: List[str]) -> bool:
    def wordBreakRecurs(s, word_dict, start):
        if start == len(s):
            return True
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_dict and wordBreakRecurs(s, word_dict, end):
                return True
        return False

    return wordBreakRecurs(s, set(wordDict), 0)


# wordBreak("leetcode", ["leet", "code"]) == True
# wordBreak("applepenapple", ["apple", "pen"]) == True
assert wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == True
