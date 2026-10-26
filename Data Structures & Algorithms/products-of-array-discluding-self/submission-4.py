class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # we awnt to prefix and suffix

        # find the prefix
        n = len(nums)
        pre = [0] * n
        suff = [0] * n
        res = [0] * n

        pre[0] = 1
        for i in range(1, n):
            pre[i] = pre[i - 1] * nums[i - 1]
        
        suff[n-1] = 1
        for i in range(n - 2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        
        for i in range(n):
            res[i] = suff[i] * pre[i]
        
        return res