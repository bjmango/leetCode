class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}

        def climb(n):
            if n in memo:
                return memo[n]
            memo[n] = climb(n - 1) + climb(n - 2)
            return memo[n]

        return climb(n)


sln = Solution()
assert sln.climbStairs(2) == 2, "expect 2"
assert sln.climbStairs(3) == 3, f"{sln.climbStairs(3)}, expect 3"
assert sln.climbStairs(5) == 8, "expect 8"

# # solution3: dynamic programing
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n in (1, 2):
#             return n
#         dp = [None] * (n + 1)
#         dp[1] = 1
#         dp[2] = 2
#         for i in range(3, n + 1):
#             dp[i] = dp[i - 1] + dp[i - 2]
#         return dp[n]


# sln = Solution()
# assert sln.climbStairs(2) == 2, "expect 2"
# assert sln.climbStairs(3) == 3, f"{sln.climbStairs(3)}, expect 3"
# assert sln.climbStairs(5) == 8, "expect 8"


# solution2, recursion + memoize
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         memo = [None] * (n + 1)
#         return self.climb(0, n, memo)

#     def climb(self, i, n, memo):
#         if i == n:
#             return 1
#         elif i > n:
#             return 0

#         if memo[i] is not None:
#             return memo[i]
#         memo[i] = self.climb(i + 1, n, memo) + self.climb(i + 2, n, memo)

#         print(f"{memo}")
#         return memo[i]


# sln = Solution()

# assert sln.climbStairs(2) == 2, "expect 2"
# assert sln.climbStairs(3) == 3, "expect 3"
# assert sln.climbStairs(5) == 8, "expect 8"


# solution1: recursion.
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         return self.climb(0, n)

#     def climb(self, i, n):
#         if i == n:
#             return 1
#         if i > n:
#             return 0
#         return self.climb(i + 1, n) + self.climb(i + 2, n)


# sln = Solution()

# assert sln.climbStairs(2) == 2, "expect 2"
# assert sln.climbStairs(3) == 3, "expect 3"
# assert sln.climbStairs(5) == 8, "expect 8"
