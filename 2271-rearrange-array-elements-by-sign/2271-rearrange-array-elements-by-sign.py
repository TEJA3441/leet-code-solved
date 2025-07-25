class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # OPTIMAL SOLUTION
        n = len(nums)
        ans = [0] * n
        pos = 0
        neg = 1

        for i in range(n):
            if nums[i] > 0:
                ans[pos] = nums[i]
                pos += 2
            else:
                ans[neg] = nums[i]
                neg += 2
            
        return ans
        
        # BRUTE SOLUTION
        # n = len(nums)
        # pos = []
        # neg = []
        
        # for i in range(n):
        #     if nums[i] >= 0:
        #         pos.append(nums[i])
        #     else:
        #         neg.append(nums[i]) 

        # for i in range(n // 2):
        #     nums[2 * i] = pos[i]
        #     nums[2 * i + 1] = neg[i]

        # return nums
