class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # OPTIMAL SOLUTION
        n = len(nums)
        cnt = 0

        for i in range(n):
            if cnt == 0:
                elmnt = nums[i]
                cnt += 1

            elif nums[i] == elmnt:
                cnt += 1
            
            else:
                cnt -= 1

        cnt1 = 0

        for i in range(n):
            if elmnt == nums[i]:
                cnt1 += 1
        if cnt1 > (n / 2):
            return elmnt
                

        # BETTER SOLUTION
        # f_array = {}
         
        # for num in nums:
        #     if num in f_array:
        #         f_array[num] += 1
        #     else:
        #         f_array[num] = 1

        # max_count = 0
        # max_element = None

        # for num, count in f_array.items():
        #     if count>max_count:
        #         max_count = count
        #         max_element = num

        # return max_element

        