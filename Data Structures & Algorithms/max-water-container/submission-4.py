class Solution:
    def maxArea(self, heights: List[int]) -> int:
        water = 0

        l, r = 0, len(heights) - 1

        while l < r:
            w = (r - l) * min(heights[l], heights[r])
            water = max(water, w)

            if heights[l] < heights[r]:
                l += 1

            else:
                r-= 1

        return water 