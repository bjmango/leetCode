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

    # solution 1:
    # def __init__(self) -> None:
    #     self.memo = {}

    # def rob(self, nums: List[int]) -> int:
    #     return self.helper(0, nums)

    # def helper(self, i, nums):
    #     if i >= len(nums):
    #         return 0
    #     if i in self.memo:
    #         return self.memo[i]
    #     # choose i or not choose i
    #     ans = max(self.helper(i + 1, nums), self.helper(i + 2, nums) + nums[i])

    #     self.memo[i] = ans
    #     return ans


sln = Solution()
print(sln.rob([2, 7, 9, 3, 1]))
print(sln.rob([]))
