class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        mpp = {}
        max_len = 0
        max_f = 0

        for r in range(n):
            mpp[s[r]] = mpp.get(s[r], 0) + 1
            max_f = max(max_f, mpp[s[r]])

            if (r - l + 1) - max_f > k:
                mpp[s[l]] -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
        
        return max_len

             
        