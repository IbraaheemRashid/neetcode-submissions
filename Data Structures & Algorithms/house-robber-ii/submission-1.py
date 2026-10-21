class Solution:
    def rob(self, nums: List[int]) -> int:
        # we cannot rob 0 and n - 1 where n is length(nums)

        if len(nums) == 1:
            return nums[0]
        
        def rob_range(start, end):
            
            memo = {}


            def dfs(i):
                if i > end:
                    return 0

                if i in memo:
                    return memo[i]

                memo[i] = max(dfs(i+1), nums[i] + dfs(i+2))
                return memo[i]
            
            return dfs(start)
        
        first = rob_range(0, len(nums)-2)
        second = rob_range(1, len(nums)-1)

        return max(first,second)
