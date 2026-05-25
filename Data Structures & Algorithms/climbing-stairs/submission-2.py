class Solution:
    def climbStairs(self, n: int) -> int:
        # to get the number of ways for n, we need the number of ways for both n-1 and n-2 (as we can move 1 or 2 steps)

        if n <= 2:
            return n
        
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]