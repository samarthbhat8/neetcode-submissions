class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for string in strs:
            hashmap = {}

            for c in string:
                hashmap[c] = hashmap.get(c, 0) + 1

            result[tuple(sorted(hashmap.items()))].append(string)

        return list(result.values())