class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        shortest = strs[0]
        length = len(strs[0])
        for s in strs:
            if len(s) < length:
                length = len(s)
                shortest = s

        for i in range(len(shortest)):
            for s in strs:
                if s[i] != shortest[i]:
                    return prefix
                
            prefix += shortest[i]

        return prefix