class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)

        for string in strs:
            hashmap = {}
            for char in string:
                hashmap[char] = 1 + hashmap.get(char, 0)
            results[tuple(sorted(hashmap.items()))].append(string)

        return list(results.values())