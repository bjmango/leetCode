from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        result = None
        hasFound = False
        for index, num in enumerate(nums):
            if num >= target:
                hasFound = True
                result = index
                break
        if hasFound:
            return result
        else:
            return len(nums)


sln = Solution()

assert sln.searchInsert([1, 3, 5, 6], 1) == 0, "should be 0"
assert sln.searchInsert([1, 3, 5, 6], 2) == 1, "should be 1"
assert sln.searchInsert([1, 3, 5, 6], 3) == 1, "should be 1"
assert sln.searchInsert([1, 3, 5, 6], 4) == 2, "should be 2"
assert sln.searchInsert([1, 3, 5, 6], 5) == 2, "should be 2"
assert sln.searchInsert([1, 3, 5, 6], 6) == 3, "should be 3"
assert sln.searchInsert([1, 3, 5, 6], 7) == 4, "should be 4"
