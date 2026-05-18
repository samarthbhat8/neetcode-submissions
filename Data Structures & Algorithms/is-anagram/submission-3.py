class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ssort = sorted(s)
        tsort = sorted(t)

        for i in range(len(s)):
            if ssort[i] != tsort[i]:
                return False

        return True


