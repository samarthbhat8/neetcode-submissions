class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        if t == "":
            return ""

        smap, tmap = {}, {}

        sub = [-1, -1]
        length = float("infinity")

        for c in range(len(t)):
            tmap[t[c]] = tmap.get(t[c], 0) + 1

        have, need = 0, len(tmap)

        left = 0
        for right in range(len(s)):
            smap[s[right]] = smap.get(s[right], 0) + 1
            
            if s[right] in tmap and smap[s[right]] == tmap[s[right]]:
                have += 1 

            while have >= need:
                if (right - left + 1) < length:
                    sub = [left, right]
                    length = right - left + 1
                
                smap[s[left]] -= 1
                
                if s[left] in tmap and smap[s[left]] < tmap[s[left]]:
                    have -= 1
                left += 1   

        return s[sub[0]:sub[1] + 1]         

                
                