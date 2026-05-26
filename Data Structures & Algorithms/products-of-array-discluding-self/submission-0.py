class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # lets make an array res of length nums
        # lets then have 2 loops right, one from before for the prefix and one for the suffix
        # then once we've done that, we just update the res array\
        n = len(nums)

        pref = [0] * n
        suf = [0] * n
        res = [0] * n

        pref[0] = suf[n-1] = 1

        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n-2, -1, -1):
            suf[i] = nums[i + 1] * suf[i + 1]
        
        for i in range(n):
            res[i] = pref[i] * suf[i]

        return res

