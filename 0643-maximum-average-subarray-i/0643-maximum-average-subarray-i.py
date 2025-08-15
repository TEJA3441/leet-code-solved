class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        window_sum = 0

        for i in range(k):
            window_sum += nums[i]
        
        left = 0
        right = k
        max_sum = window_sum

        while right < n:
            window_sum = window_sum - nums[left] + nums[right]

            if window_sum > max_sum:
                max_sum = window_sum
            
            left += 1
            right += 1
        
        return max_sum / k



        

        