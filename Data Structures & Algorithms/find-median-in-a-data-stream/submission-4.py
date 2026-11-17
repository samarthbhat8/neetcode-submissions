class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        
        if (self.maxHeap and self.minHeap) and -self.maxHeap[0] > self.minHeap[0]:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        if len(self.minHeap) > len(self.maxHeap) + 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def findMedian(self) -> float:
        
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        
        elif len(self.minHeap) < len(self.maxHeap):
            return -self.maxHeap[0]
        
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2