class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t in ('+', '-', '*', '/'):
                op = t
                second = int(stack.pop())
                first = int(stack.pop())

                if op == "+":
                    val = first + second
                    stack.append(str(val))
                
                if op == "-":
                    val = first - second
                    stack.append(str(val))

                if op == "*":
                    val = first * second
                    stack.append(str(val))

                if op == "/":
                    val = int(float(first) / second)
                    stack.append(str(val))

            else:
                stack.append(t)

        return int(stack[0])