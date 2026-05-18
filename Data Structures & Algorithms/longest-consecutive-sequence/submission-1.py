class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for i in nums:
            if i - 1 not in numSet:
                consecutive = 0
                while i + consecutive in numSet:
                    consecutive += 1

                longest = max(longest, consecutive)

        return longest
