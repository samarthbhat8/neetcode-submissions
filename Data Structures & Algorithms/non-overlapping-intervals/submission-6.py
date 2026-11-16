class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[1])
        overlaps = 0
        prevEnd = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] < prevEnd:
                overlaps += 1

            else:
                prevEnd = intervals[i][1]

        return overlaps