class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        count = 0
        sums = {0 : 1}

        for num in nums:

            total += num

            if (total - k) in sums:
                count += sums[total - k]
            
            if total in sums:
                sums[total] += 1
            else:
                sums[total] = 1
        
        return count
                
        