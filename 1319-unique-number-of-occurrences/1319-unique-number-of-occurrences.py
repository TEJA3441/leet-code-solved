class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        n = len(arr)
        hash_map = {}

        for i in range(n):
            val = arr[i]
            if val in hash_map:
                
                hash_map[val] += 1
            
            else:
                hash_map[val] = 1
        
        occurences = list(hash_map.values())

        return len(occurences) == len(set(occurences))
        
    





        