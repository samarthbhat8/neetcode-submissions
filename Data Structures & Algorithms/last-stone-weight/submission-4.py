class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            maxHeap.append(-stone)
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            first = heapq.heappop(maxHeap)
            second = heapq.heappop(maxHeap)

            if first != second:
                heapq.heappush(maxHeap, first - second)

        if maxHeap:
            return abs(maxHeap[0])

        return 0