class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        count = [[] for i in range(len(nums) + 1)]

        for n in nums:
            hashmap[n] = 1 + hashmap.get(n, 0)

        for number, frequency in hashmap.items():
            count[frequency].append(number)

        result = []
        for i in range(len(count) - 1, -1, -1):
            if len(result) == k:
                return result

            if count[i]:
                for n in count[i]:
                    result.append(n)

        