class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = 0
        suffix = 0
        max_product = float('-inf')

        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            
            prefix *= nums[i]
            suffix *= nums[n - i - 1]
            max_product = max(max_product, max(prefix, suffix))
        
        return max_product

        