class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seenS = {}
        seenT = {}
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            seenS[s[i]] = seenS.get(s[i], 0) + 1
            seenT[t[i]] = seenT.get(t[i], 0) + 1

        return seenS == seenT