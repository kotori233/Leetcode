class Solution(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            dp[i] = 0x7FFFFFFF
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[n]