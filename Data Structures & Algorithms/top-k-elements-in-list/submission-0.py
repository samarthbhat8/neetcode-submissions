class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for number, c in count.items():
            frequency[c].append(number)

        result = []
        for i in range(len(frequency) - 1, -1, -1):
            if len(result) == k:
                return result
            
            for x in frequency[i]:
                result.append(x)