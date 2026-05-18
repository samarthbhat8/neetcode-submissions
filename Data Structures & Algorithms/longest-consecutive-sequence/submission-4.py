class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longest = 0

        for n in nums:
            number = n
            length = 1
            while (number + 1) in numSet:
                length += 1
                number += 1
            longest = max(longest, length)


        return longest