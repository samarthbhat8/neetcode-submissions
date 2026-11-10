class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        freq = [[] for i in range(len(nums) + 1)]

        for n, f in count.items():
            freq[f].append(n)

        result = []
        i = len(freq) - 1
        while len(result) < k:
            for num in freq[i]:
                result.append(num)
            i -= 1

        return result

