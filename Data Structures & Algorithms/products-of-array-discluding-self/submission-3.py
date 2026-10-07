class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # go through the whole array, keep a count of which number on
        # skip that number and then append to new array

        # instead waht we can do is have a prefix and a suffix
        # prefix array and suffix array

        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n-1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i-1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        
        return res
