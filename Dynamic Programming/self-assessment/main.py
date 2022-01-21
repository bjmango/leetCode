class Solution:

    # solution3:
    # 1   1   1   1
    # 1   2   3   4
    # 1   3   6   10
    # 1   4   10  20
    def count_path(self, n: int) -> int:
        if n == 1:
            return 1
        result = [[1 for _ in range(n)] for _ in range(n)]
        for r in range(1, n):
            for c in range(1, n):
                result[r][c] = result[r - 1][c] + result[r][c - 1]
        print(result)
        return result[n - 1][n - 1]


sln = Solution()
assert sln.count_path(1) == 1, f"sln.count_path(1) = {sln.count_path(1)} expect 1"
assert sln.count_path(2) == 2, f"sln.count_path(1) = {sln.count_path(2)} expect 2"
assert sln.count_path(3) == 6, f"sln.count_path(1) = {sln.count_path(3)} expect 6"
assert sln.count_path(4) == 20, f"sln.count_path(1) = {sln.count_path(4)} expect 20"
assert sln.count_path(5) == 70, f"sln.count_path(1) = {sln.count_path(5)} expect 70"


# solution2： side note: 逆序range() - range(10， 0， -1)
# 20  10   4   1
# 10   6   3   1
# 4   3   2   1
# 1   1   1   1

#     def count_path(self, n: int) -> int:
#         if n == 1:
#             return 1
#         result = [[1 for _ in range(n)] for _ in range(n)]
#         for r in range(n - 2, -1, -1):
#             for c in range(n - 2, -1, -1):
#                 result[r][c] = result[r + 1][c] + result[r][c + 1]
#         print(result)
#         return result[0][0]


# sln = Solution()
# assert sln.count_path(1) == 1, f"sln.count_path(1) = {sln.count_path(1)} expect 1"
# assert sln.count_path(2) == 2, f"sln.count_path(1) = {sln.count_path(2)} expect 2"
# assert sln.count_path(3) == 6, f"sln.count_path(1) = {sln.count_path(3)} expect 6"
# assert sln.count_path(4) == 20, f"sln.count_path(1) = {sln.count_path(4)} expect 20"
# assert sln.count_path(5) == 70, f"sln.count_path(1) = {sln.count_path(5)} expect 70"
# def count_path(self, m: int, n: int) -> int:
#     if m == 1 and n == 1:
#         return 1
#     result = [[1 for _ in range(n)] for _ in range(m)]
#     print(result)
#     for r in range(m - 1):
#         for c in range(n - 1):
#             result[r][c] = result(r - 1, c) + result(r, c - 1)

#     return result[0][0]


# sln = Solution()
# print(sln.count_path(1, 1))
# assert sln.count_path(1, 1) == 1, f"sln.count_path(1,1) = {sln.count_path(1,1)} expect 1"
# print(sln.count_path(2, 2))
# assert sln.count_path(2, 2) == 2, f"(2,2) expect 2"
# print(sln.count_path(3, 3))
# assert sln.count_path(3, 3) == 6, f"(3,3) expect 6"

# def countPaths(row: int, col: int, n: int, memo: dict) -> int:
# if not (row <= n - 1 and col <= n - 1):
#     return 0

# if row == n - 1 and col == n - 1:
#     return 1

# if memo.get((row, col), None) is not None:
#     return memo[(row, col)]

# memo[(row, col)] = countPaths(row + 1, col, n, memo) + countPaths(row, col + 1, n, memo)
# return memo[(row, col)]


# def is_in_grid(row, col, n):
#     return row <= n - 1 and col <= n - 1


# def is_at_end(row, col, n):
#     return row == n - 1 and col == n - 1


# def main(row, col, n):
#     memo = {}
#     return countPaths(row, col, n, memo)


# if __name__ == "__main__":
#     assert main(0, 0, 1) == 1, "expect 1"
#     assert main(0, 0, 2) == 2, "expect 2"
#     assert main(0, 0, 3) == 6, f"{countPaths(0,0,3)}expect 6"
