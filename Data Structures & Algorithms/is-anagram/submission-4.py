class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # we could sort each and compare but thats nto the best
        # we should check the lengths - if theyre not equal then return false
        # then we should loop through each and add every letter to a hashmap for each
        # then return the hashmap comparison

        seenS = {}
        seenT = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            seenS[s[i]] = 1 + seenS.get(s[i], 0)
            seenT[t[i]] = 1 + seenT.get(t[i], 0)
        
        return seenS == seenT
