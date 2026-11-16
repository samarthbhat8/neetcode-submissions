class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []

        for p in points:
            x, y = p[0], p[1]
            distance = -(x**2 + y**2)

            heapq.heappush(maxHeap, [distance, x, y])

            while len(maxHeap) > k:
                heapq.heappop(maxHeap)

        result = []
        while len(result) < k:
            distance, x, y = heapq.heappop(maxHeap)
            result.append([x, y])

        return result