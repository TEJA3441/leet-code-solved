class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = 0
        current_sum = 0
        min_len = float('inf')

        while right < n:
            current_sum += nums[right]

            while current_sum >= target:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len

                current_sum -= nums[left]
                left += 1
                
            right += 1
        
        if min_len == float('inf'):

            return 0

        return min_len
            
