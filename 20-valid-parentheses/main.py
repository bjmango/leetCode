class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open_map = {']': '[', ')': '(', '}': '{'}

        for c in s:
            if c in close_to_open_map:
                if stack and stack[-1] == close_to_open_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return not stack


sln = Solution()
assert sln.isValid('')
assert sln.isValid('{{{}}}')
assert not sln.isValid('[][')
