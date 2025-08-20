class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atmost(k):
            n = len(nums)
            left = 0
            count = 0
            odd = 0

            for right in range(n):

                if nums[right] % 2 == 1:
                    odd += 1
                
                while odd > k:
                    if nums[left] % 2 == 1:
                        odd -= 1

                    left += 1
                
                count += (right - left + 1)
            
            return count
        
        return atmost(k) - atmost(k - 1)
