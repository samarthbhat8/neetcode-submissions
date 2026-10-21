class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        map = {')' : '(', ']' : '[', '}' : '{'}

        for p in s:
            if p in map:
                if stack and stack[-1] == map[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)

        return not stack