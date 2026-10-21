class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        map = {')' : '(', ']' : '[', '}' : '{'}

        for p in s:
            if p not in map:
                stack.append(p)
            elif not stack or stack[-1] != map[p]:
                return False
            else:
                stack.pop()

        return not stack