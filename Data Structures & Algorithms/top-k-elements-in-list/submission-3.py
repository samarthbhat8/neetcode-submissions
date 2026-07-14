class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        frequency = [[] for i in range(len(nums) + 1)]

        for n, count in count.items():
            frequency[count].append(n)

        results = []
        for i in range(len(frequency) - 1, -1, -1):
            if len(results) < k:
                for n in frequency[i]:
                    results.append(n)

        return results