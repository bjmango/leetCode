from lib2to3.pgen2.token import SLASHEQUAL
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        memo = [[1 for _ in range(i + 1)] for i in range(numRows)]
        if numRows in (0, 1):
            return memo
        for row in range(2, numRows):
            for col in range(1, len(memo[row - 1])):
                memo[row][col] = memo[row - 1][col - 1] + memo[row - 1][col]
        return memo


sln = Solution()

# print(sln.generate(1))
# print(sln.generate(2))
print(sln.generate(3))
print(sln.generate(4))
print(sln.generate(5))
