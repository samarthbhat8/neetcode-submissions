class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for i in range(len(s)):
                count[ord(s[i]) - ord("a")] += 1
            hashmap[tuple(count)].append(s)

        return list(hashmap.values())


        