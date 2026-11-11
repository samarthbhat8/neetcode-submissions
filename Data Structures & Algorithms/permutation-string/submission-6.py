class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        hashmap1, hashmap2 = {}, {}
            
        for s in range(len(s1)):
            hashmap1[s1[s]] = hashmap1.get(s1[s], 0) + 1
            hashmap2[s2[s]] = hashmap2.get(s2[s], 0) + 1

        l = 0
        for r in range(len(s1), len(s2)):
            if hashmap1 == hashmap2:
                return True

            hashmap2[s2[r]] = hashmap2.get(s2[r], 0) + 1
            hashmap2[s2[l]] -= 1
            if hashmap2[s2[l]] == 0:
                del hashmap2[s2[l]]
            l += 1

        return hashmap1 == hashmap2

            
