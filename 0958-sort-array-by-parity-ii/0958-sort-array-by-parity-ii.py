class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        n = len(nums)
        evn = 0
        odd = 1
        ans = [0] * n

        for i in range(n):
            if nums[i] % 2 == 0:
                ans[evn] = nums[i]
                evn += 2
            else:
                ans[odd] = nums[i]
                odd += 2
        
        return ans
                 