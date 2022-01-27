from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = rob2 = 0
        # [rob1, rob2, n, n+1, .... ]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


sln = Solution()
print(sln.rob([2, 7, 9, 3, 1]))
print(sln.rob([]))
