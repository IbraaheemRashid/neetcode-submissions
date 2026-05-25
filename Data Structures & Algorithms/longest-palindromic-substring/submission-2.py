class Solution:
    def longestPalindrome(self, s: str) -> str:
        # ababd, ab aba is abab ababa ababd bab babd ba bb
        resIndex = 0
        resLength = 0

        for i in range(len(s)):
            l, r = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLength:
                    resLength = r - l + 1
                    resIndex = l
                l -= 1
                r += 1

            l, r = i, i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLength:
                    resLength = r - l + 1
                    resIndex = l
                l -= 1
                r += 1
        
        return s[resIndex: resIndex + resLength]