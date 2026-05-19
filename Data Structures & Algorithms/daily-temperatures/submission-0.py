class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0 for i in range(len(temperatures))]
        stack = []

        for t in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[t]:
                stackt, stacki = stack.pop() 
                results[stacki] = t - stacki
            stack.append((temperatures[t], t))


        return results