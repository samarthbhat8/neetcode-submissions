class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            maxHeap.append([-(x**2 + y**2), x, y])
        heapq.heapify(maxHeap)

        while len(maxHeap) > k:
            heapq.heappop(maxHeap)

        result = []
        while maxHeap:
            distance, x, y = heapq.heappop(maxHeap)
            result.append([x, y])
        
        return result