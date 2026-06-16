class Solution:
    def climbStairs(self, n: int) -> int:
        #1+1+1
        #1+2+1
        #2+1+2
        #ones, onetT, twoO = 0, 0, 0
        if n <= 2:
            return n
        one, two = 1, 1
        for i in range(n - 1):
            tmp = one
            one = one + two
            two = tmp
        return one