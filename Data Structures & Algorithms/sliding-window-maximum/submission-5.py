class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        maxHeap = []

        for i in range(k):
            heapq.heappush(maxHeap, (-nums[i], i))

        result.append(-maxHeap[0][0])

        for r in range(k, len(nums)):
            while maxHeap and maxHeap[0][1] < r - k + 1:
                heapq.heappop(maxHeap)

            heapq.heappush(maxHeap, (-nums[r], r))
            result.append(-maxHeap[0][0])

            

        return result