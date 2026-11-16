class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}

        for t in tasks:
            count[t] = 1 + count.get(t, 0)

        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        queue = deque()
        time = 0

        while maxHeap or queue:
            time += 1
            if maxHeap:
                c = 1 + heapq.heappop(maxHeap)
                if c != 0:
                    queue.append([c, time + n])

            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time