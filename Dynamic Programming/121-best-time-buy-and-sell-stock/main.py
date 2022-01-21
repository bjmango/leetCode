from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit


sln = Solution()
assert sln.maxProfit([1, 2, 4, 5, 1]) == 4, "expect 4"
assert sln.maxProfit([7, 1, 2, 4, 5, 1]) == 4, "expect 4"
assert sln.maxProfit([1, 2, 4, 1, 2, 5, 1]) == 4, "expect 4"
assert sln.maxProfit([1]) == 0, "expect 0"
assert sln.maxProfit([1, 1]) == 0, "expect 0"
assert sln.maxProfit([5, 1]) == 0, "expect 0"
