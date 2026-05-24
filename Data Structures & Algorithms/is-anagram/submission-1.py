class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = {}
        hash2 = {}

        for i in range(len(s)):
            if s[i] in hash1:
                hash1[s[i]] += 1
            else:
                hash1[s[i]] = 1
        
        for j in range(len(t)):
            if t[j] in hash2:
                hash2[t[j]] += 1
            else:
                hash2[t[j]] = 1

        return hash1 == hash2