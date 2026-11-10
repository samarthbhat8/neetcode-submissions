class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count1 = [0] * 26
        count2 = [0] * 26

        for c in range(len(s)):
            count1[ord(s[c]) - ord("a")] += 1
            count2[ord(t[c]) - ord("a")] += 1

        for i in range(len(count1)):
            if count1[i] != count2[i]:
                return False

        return True
        