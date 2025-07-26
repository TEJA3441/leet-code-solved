class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest = 0

        for num in set_nums:
            if num - 1 not in set_nums:
                current = num
                count = 1
            
                while current + 1 in set_nums:
                    current += 1
                    count += 1
            
                longest = max(longest, count)
        
        return longest
        