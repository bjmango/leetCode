class Solution:
    # solution3. dynamic programing
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        memo = [[False for _ in range(length)] for _ in range(length)]
        start = 0
        max_length = 1

        for i in range(length - 1):
            memo[i][i] = True

        for end_index in range(length):
            for start_index in range(end_index):
                if s[end_index] != s[start_index]:
                    memo[start_index][end_index] = False
                else:
                    if end_index - start_index < 3:
                        memo[start_index][end_index] = True
                    else:
                        memo[start_index][end_index] = memo[start_index + 1][end_index - 1]

                if memo[start_index][end_index] and end_index - start_index + 1 > max_length:
                    start = start_index
                    max_length = end_index - start_index + 1
        return s[start : start + max_length]


sln = Solution()
assert sln.longestPalindrome("babad") == "bab", f"actual = {sln.longestPalindrome('babad')}; expect = bab"
assert sln.longestPalindrome("cbbd") == "bb", f"actual = {sln.longestPalindrome('cbbd')}; expect = bb"
assert sln.longestPalindrome("a") == "a", f"actual = {sln.longestPalindrome('a')}; expect = a"
assert sln.longestPalindrome("bb") == "bb", f"actual = {sln.longestPalindrome('bb')}; expect = bb"
assert sln.longestPalindrome("ab") == "a", f"actual = {sln.longestPalindrome('ab')}; expect = a"

# solution2: use dictionary to memoize
#     def longestPalindrome(self, s: str) -> str:
#         memo = {}
#         length = len(s)
#         if length in (0, 1):
#             return s
#         if length == 2:
#             return s if s[0] == s[1] else s[0]
#         for i in range(length):
#             start_index = i
#             for j in range(i + 1, length + 1):
#                 current_index = j
#                 sub_str = s[start_index:current_index]
#                 if memo.get(sub_str) is None and sub_str == sub_str[::-1]:
#                     memo[sub_str] = len(sub_str)
#         print(memo)
#         return max(memo, key=memo.get)

# sln = Solution()
# assert sln.longestPalindrome("babad") == "bab", f"actual = {sln.longestPalindrome('babad')}; expect = bab"
# assert sln.longestPalindrome("cbbd") == "bb", f"actual = {sln.longestPalindrome('cbbd')}; expect = bb"
# assert sln.longestPalindrome("a") == "a", f"actual = {sln.longestPalindrome('a')}; expect = a"
# assert sln.longestPalindrome("bb") == "bb", f"actual = {sln.longestPalindrome('bb')}; expect = bb"
# assert sln.longestPalindrome("ab") == "a", f"actual = {sln.longestPalindrome('ab')}; expect = a"

# solution1  Time Limit Exceeded
# def longestPalindrome(self, s: str) -> str:
#     length = len(s)
#     longest = 0
#     longest_sub = ""
#     if length in (0, 1):
#         return s
#     if length == 2:
#         return s if s[0] == s[1] else s[0]
#     for i in range(length):
#         start_index = i
#         for j in range(len(s) + 1, i + 1, -1):
#             current_index = j
#             sub_str = s[start_index:current_index]
#             if len(sub_str) > longest and len(self.isPalindrome(sub_str)) > longest:
#                 longest = len(self.isPalindrome(sub_str))
#                 longest_sub = self.isPalindrome(sub_str)
#                 break
#     return longest_sub

# def isPalindrome(self, sub_str):
#     length = len(sub_str)
#     for i in range(int(length / 2) + 1):
#         if sub_str[i] != sub_str[length - 1 - i]:
#             return ""
#     return sub_str

# sln = Solution()
# print(sln.longestPalindrome("babad"))
# print(sln.longestPalindrome("cbbd"))
# print(sln.longestPalindrome("a"))
# print(sln.longestPalindrome("bb"))
# assert sln.longestPalindrome("babad") == "bab", f"actual = {sln.longestPalindrome('babad')}; expect = bab"
# assert sln.longestPalindrome("cbbd") == "bb", f"actual = {sln.longestPalindrome('cbbd')}; expect = bb"
# assert sln.longestPalindrome("a") == "a", f"actual = {sln.longestPalindrome('a')}; expect = a"
# assert sln.longestPalindrome("bb") == "bb", f"actual = {sln.longestPalindrome('bb')}; expect = bb"
# assert sln.longestPalindrome("ab") == "a", f"actual = {sln.longestPalindrome('ab')}; expect = a"


#     3 CHANG solution
#     def longestPalindrome(self, s: str) -> str:
#         dp = [[False for _ in range(len(s))] for _ in range(len(s))]
#         start = 0
#         length = 1
#         for i in range(len(s)):
#             dp[i][i] = True
#         for i in range(len(s) - 1):
#             if s[i] == s[i + 1]:
#                 start = i
#                 length = 2
#                 dp[i][i + 1] = True
#         for k in range(3, len(s) + 1):
#             for i in range(len(s) - k + 1):
#                 j = k + i - 1
#                 if dp[i + 1][j - 1] and s[i] == s[j]:
#                     dp[i][j] = True
#                     if k > length:
#                         start = i
#                         length = k
#         return s[start : start + length]


# sln = Solution()
# assert sln.longestPalindrome("babad") == "bab", f"actual = {sln.longestPalindrome('babad')}; expect = bab"
# assert sln.longestPalindrome("cbbd") == "bb", f"actual = {sln.longestPalindrome('cbbd')}; expect = bb"
# assert sln.longestPalindrome("a") == "a", f"actual = {sln.longestPalindrome('a')}; expect = a"
# assert sln.longestPalindrome("bb") == "bb", f"actual = {sln.longestPalindrome('bb')}; expect = bb"
# assert sln.longestPalindrome("ab") == "a", f"actual = {sln.longestPalindrome('ab')}; expect = a"
