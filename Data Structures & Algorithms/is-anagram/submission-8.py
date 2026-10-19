class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        smap, tmap = {}, {}
        for c in range(len(s)):
            smap[s[c]] = smap.get(s[c], 0) + 1
            tmap[t[c]] = tmap.get(t[c], 0) + 1

        for c in smap.keys():
            if smap.get(c, 0) != tmap.get(c, 0):
                return False
            
        return True