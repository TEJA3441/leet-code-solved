class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        hash_map = {}

        for i in range(n):
            more = target - nums[i]
            if more in hash_map:
                return [hash_map[more], i]
            hash_map[nums[i]] = i
        
        return []




        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):

        #         if nums[i] + nums[j] == target:

        #             return [i, j]
        # return []
        