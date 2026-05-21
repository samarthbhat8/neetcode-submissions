class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left <= right:
            middle = (left + right) // 2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / middle)
            
            if hours <= h: # more time is left meaning less bananas can be ate
                k = middle
                right = middle - 1

            else: # not enought time meaning more bananas need to be ate
                left = middle + 1
        
        return k