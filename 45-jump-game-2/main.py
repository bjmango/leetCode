from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        left = right = 0
        while right < len(nums) - 1:
            farest = 0
            for i in range(left, right + 1):
                farest = max(farest, i + nums[i])
            left = right + 1
            right = farest
            jumps += 1
        return jumps


sln = Solution()
assert sln.jump([2, 3, 1, 1, 4]) == 2
assert sln.jump([2, 3, 1, 1, 4]) == 2
assert sln.jump([3, 3, 0, 1, 4]) == 2
assert sln.jump([3, 1, 1, 4]) == 1
assert sln.jump([1, 1, 1, 1]) == 3
