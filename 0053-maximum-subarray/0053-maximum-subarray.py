class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # OPTIMAL

        n = len(nums)
        sum1 = 0
        max_sum = float('-inf')

        for i in range(n):
            sum1 += nums[i]
            if sum1 > max_sum:
                max_sum = sum1
            if sum1 < 0:
                sum1 = 0
        
        return max_sum




        
        # for smaller arrays

        # n = len(nums)
        # max_sum = float('-inf')

        # for i in range(n):
        #     sum1 = 0
        #     for j in range(i, n):
        #         sum1 += nums[j]
        #         max_sum = max(sum1, max_sum)

        # return max_sum
        