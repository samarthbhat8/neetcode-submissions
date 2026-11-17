class MedianFinder:

    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        self.array.append(float(num))

    def findMedian(self) -> float:
        if len(self.array) == 1:
            return self.array[0]

        self.array.sort()

        middle = len(self.array) // 2

        if len(self.array) % 2 == 0:
            return (self.array[middle - 1] + self.array[middle]) / 2
        
        return self.array[middle]