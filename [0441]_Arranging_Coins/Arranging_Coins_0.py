class Solution(object):

    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt
        return int(sqrt(2 * n + 0.25) - 0.5)
