class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len is not same, then not anagram
        # if characters are all the same then valid
        # we can have a hashmap for each and then compare

        if len(s) != len(t):
            return False
        
        charT = {}
        charS = {}

        for i in range(len(s)):
            charS[s[i]] = 1 + charS.get(s[i], 0)
            charT[t[i]] = 1 + charT.get(t[i], 0)

        return charS == charT