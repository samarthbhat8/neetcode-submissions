class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for n in range(len(nums)):
            if target - nums[n] in hashmap:
                return [hashmap[target - nums[n]], n]
            
            hashmap[nums[n]] = n