class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap1, hashmap2 = {}, {}

        for c in range(len(s)):
            hashmap1[s[c]] = 1 + hashmap1.get(s[c], 0)
            hashmap2[t[c]] = 1 + hashmap2.get(t[c], 0)

        for c in range(len(s)):
            if hashmap1[s[c]] != hashmap2.get(s[c], 0):
                return False

        return True