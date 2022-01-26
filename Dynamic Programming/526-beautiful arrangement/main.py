from itertools import permutations


class Solution:
    # solution2: 相比第一种暴力的遍历所有permutation，判断每一个的结果。
    # 这个方法改变了思路，主动来生成符合条件的 permutation， 避免了很多的迭代。
    # 只有把possible_numbers列表中的数字都耗尽了，说明才是是符合条件的permutation。
    def countArrangement(self, n: int) -> int:
        possible_numbers = [i for i in range(1, n + 1)]
        return self.recursion(possible_numbers, 1)

    def recursion(self, possible_numbers, index):
        if len(possible_numbers) == 0:
            return 1
        result = 0
        for i in range(len(possible_numbers)):
            if possible_numbers[i] % index == 0 or index % possible_numbers[i] == 0:
                result += self.recursion(possible_numbers[:i] + possible_numbers[i + 1 :], index + 1)
        return result


sln = Solution()
assert sln.countArrangement(1) == 1, f"actual {sln.countArrangement(1)}; expect 1"
assert sln.countArrangement(2) == 2, f"actual {sln.countArrangement(2)}; expect 2"
assert sln.countArrangement(3) == 3, f"actual {sln.countArrangement(3)}; expect 3"
assert sln.countArrangement(4) == 8, f"actual {sln.countArrangement(4)}; expect 8"
assert sln.countArrangement(5) == 10, f"actual {sln.countArrangement(5)}; expect 10"
assert sln.countArrangement(6) == 36, f"actual {sln.countArrangement(6)}; expect 36"
assert sln.countArrangement(7) == 41, f"actual {sln.countArrangement(7)}; expect 41"
assert sln.countArrangement(8) == 132, f"actual {sln.countArrangement(8)}; expect 132"
assert sln.countArrangement(9) == 250, f"actual {sln.countArrangement(9)}; expect 250"
assert sln.countArrangement(10) == 700, f"actual {sln.countArrangement(10)}; expect 700"
assert sln.countArrangement(11) == 750, f"actual {sln.countArrangement(11)}; expect 750"
assert sln.countArrangement(12) == 4010, f"actual {sln.countArrangement(12)}; expect 4010"
assert sln.countArrangement(13) == 4237, f"actual {sln.countArrangement(13)}; expect 4237"
assert sln.countArrangement(14) == 10680, f"actual {sln.countArrangement(14)}; expect 10680"
assert sln.countArrangement(15) == 24679, f"actual {sln.countArrangement(15)}; expect 24679"
