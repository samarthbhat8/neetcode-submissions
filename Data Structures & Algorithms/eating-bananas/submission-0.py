class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        hours = right

        while left <= right:
            mid = (left + right) // 2
            k = 0

            for i in range(len(piles)):
                k += math.ceil(float(piles[i]) / mid)

            if k <= h:
                hours = mid
                right = mid - 1

            else:
                left = mid + 1

        return hours
