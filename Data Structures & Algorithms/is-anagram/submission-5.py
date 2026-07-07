class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        smap, tmap = {}, {}

        for c in range(len(s)):
            smap[s[c]] = 1 + smap.get(s[c], 0)
            tmap[t[c]] = 1 + tmap.get(t[c], 0)

        return smap == tmap