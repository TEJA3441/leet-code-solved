class Solution:
    def twoSum(self, arr, target):
        n = len(arr)
        hash_map = {}

        for i in range(n):
            more = target - arr[i]

            if  more in hash_map:
                return [hash_map[more], i]
            
            hash_map[arr[i]] = i
        
        return []




        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):

        #         if nums[i] + nums[j] == target:

        #             return [i, j]
        # return []
        