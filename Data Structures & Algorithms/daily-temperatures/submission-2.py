class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0 for i in range(len(temperatures))]
        stack = [] # [temperature, index]

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                temp, index = stack.pop()
                days[index] = i - index
                
            stack.append([temperatures[i], i]) 
            

        return days