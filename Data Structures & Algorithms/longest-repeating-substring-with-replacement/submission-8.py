class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        length = 0
        hashmap = [0] * 26 # letter : frequency
        frequency = 0

        for r in range(len(s)):
            hashmap[ord(s[r]) - ord("A")] += 1
            if hashmap[ord(s[r]) - ord("A")] > frequency:
                frequency = hashmap[ord(s[r]) - ord("A")]

            while (r - l + 1) - frequency > k:
                hashmap[ord(s[l]) - ord("A")] -= 1
                l += 1
            
            length = max(length, r - l + 1)

        return length