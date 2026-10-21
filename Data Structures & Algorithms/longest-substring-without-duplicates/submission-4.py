class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        l = r = 0

        length = 0
        char = set()
        
        while r < len(s):
            while s[r] in char:
                char.remove(s[l])
                l += 1

            char.add(s[r])
            length = max(length, r - l + 1)
            r += 1

        return length


