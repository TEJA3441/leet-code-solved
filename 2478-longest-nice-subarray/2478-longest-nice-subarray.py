class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        curr = 0
        res = 0

        for right in range(n):
            # Shrink window until nums[right] can be added
            while curr & nums[right]:
                curr ^= nums[left]
                left += 1
            
            # Add nums[right] to the window
            curr |= nums[right]

            # Update result
            res = max(res, right - left + 1)
        
        return res
