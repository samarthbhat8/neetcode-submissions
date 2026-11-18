class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        tcount = {}
        scount = {}

        result = [-1, -1]
        length = float("inf")

        for i in range(len(t)):
            tcount[t[i]] = 1 + tcount.get(t[i], 0)

        need = len(tcount)
        have = 0

        l = 0

        for r in range(len(s)):
            scount[s[r]] = 1 + scount.get(s[r], 0)
            if s[r] in tcount and scount[s[r]] == tcount[s[r]]:
                have += 1

            while have == need:
                if (r - l + 1) < length:
                    result = [l, r + 1]
                    length = r - l + 1

                scount[s[l]] -= 1
                if s[l] in tcount and scount[s[l]] < tcount[s[l]]:
                    have -= 1
                l += 1

        l, r = result
        if length != float("inf"):
            return s[l:r]
        return ""
