class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # OPTIMAL

        n = len(nums)
        curr_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, n):
            curr_sum = max(nums[i], curr_sum + nums[i])

            max_sum = max(curr_sum, max_sum)

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
        