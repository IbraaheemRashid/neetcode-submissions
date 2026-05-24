class Solution:
    def isPalindrome(self, s: str) -> bool:
        # go through the string with 2 pointers
        # if i is a space then continue
        # otherwise compare each pointer
        # if at any point the pointers arent equal then false
                # if the pointers reach each other and everything was equal then return true
        l, r = 0, len(s) - 1
        s = s.lower()

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1

            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False

        return True
