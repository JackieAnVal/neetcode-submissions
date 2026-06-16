class Solution:
    def climbStairs(self, n: int) -> int:
        #1+1+1
        #1+2+1
        #2+1+2
        #ones, onetT, twoO = 0, 0, 0
        if n <= 2:
            return n
        dp = [1, 2]    
        for i in range(n - 2):
            temp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = temp
        return dp[1]