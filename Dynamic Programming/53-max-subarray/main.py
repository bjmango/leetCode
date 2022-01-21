from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 方法： 追踪
        max_sub = nums[0]
        current_sub = nums[0]
        for x in nums[1:]:
            if current_sub >= 0:
                current_sub += x
            else:
                current_sub = x
            max_sub = max(current_sub, max_sub)
        return max_sub

        # 等价方法2. max(current_sub + x, x) 等价于判断 current_sub + x - x = current_sub 大于0 还是小于0
        # 如果结果（current_sub）大于0， 结果就是 current_sub + x, 结果小于0， 结果就是x
        max_sub = nums[0]
        current_sub = nums[0]

        for x in nums[1:]:
            current_sub = max(current_sub + x, x)
            max_sub = max(max_sub, current_sub)
        return max_sub


sln = Solution()

sln.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, "expect 6"
sln.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -6, 7]) == 7, "expect 7"
