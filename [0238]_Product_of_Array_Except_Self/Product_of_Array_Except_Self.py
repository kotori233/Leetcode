class Solution(object):

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1 for i in range(n)]
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        temp = 1
        for i in range(n - 2, -1, -1):
            temp *= nums[i + 1]
            res[i] *= temp
        return res
