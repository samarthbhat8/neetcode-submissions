class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = []
        for stone in stones:
            s.append(-stone)
        
        heapq.heapify(s)

        while len(s) > 1:
            heapq.heappush(s, (heapq.heappop(s) - heapq.heappop(s)))

        return -s[0] if s else 0