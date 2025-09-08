class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        r = 0
        max_len = 0
        zeros = 0

        while r < n:
            if nums[r] == 0:
                zeros += 1

            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            if zeros <= k:
                len1 = r - l + 1
                max_len = max(max_len, len1)

            r += 1
        
        return max_len
