class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = 1
        res = nums[0]

        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
                res = max(res, 0)
                continue

            temp = curMax * n

            curMax = max(n, curMax * n, curMin * n)
            curMin = min(n, temp, curMin * n)

            res = max(res, curMax)

        return res