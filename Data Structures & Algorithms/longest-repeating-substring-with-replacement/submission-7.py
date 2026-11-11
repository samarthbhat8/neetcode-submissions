class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        length = 0
        hashmap = {} # letter : frequency
        frequency = 0

        for r in range(len(s)):
            hashmap[s[r]] = hashmap.get(s[r], 0) + 1
            if hashmap[s[r]] > frequency:
                frequency = hashmap[s[r]]

            while (r - l + 1) - frequency > k:
                hashmap[s[l]] -= 1
                l += 1
            
            length = max(length, r - l + 1)

        return length