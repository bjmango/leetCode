from typing import List


def singleNumber(nums: List[int]) -> int:
    a = 0
    for num in nums:
        a ^= num
    return a


assert singleNumber([2, 2, 1]) == 1, "expect 1"
assert singleNumber([4, 1, 2, 1, 2]) == 4, "expect 4"
assert singleNumber([2, 2, 1]) == 1, "expect 1"
assert singleNumber([2, 2, 4]) == 4, "expect 4"
