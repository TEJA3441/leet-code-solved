class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l_sum = 0
        r_sum = 0

        for i in range(k):
            l_sum += nums[i]
            
        max_sum = l_sum
        
        ri_index = n-1

        for j in range(k-1, -1, -1):
            l_sum -= nums[j]
            r_sum += nums[ri_index]
            ri_index -= 1

            max_sum = max(max_sum, l_sum + r_sum)
        
        return max_sum
        