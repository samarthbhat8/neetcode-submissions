class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for n in range(len(nums)):
            value = target - nums[n]
            if value in values:
                return [values[value], n]
            values[nums[n]] = n