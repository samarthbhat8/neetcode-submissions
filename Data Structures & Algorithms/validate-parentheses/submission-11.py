class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {'}' : '{', ')' : '(', ']' : '['}

        stack = []
        for b in s:
            if b in hashmap:
                if stack:
                    if stack[-1] == hashmap[b]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False

            else:
                stack.append(b)

        return not stack

        