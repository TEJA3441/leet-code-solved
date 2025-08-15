class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        left = 0
        right = 0
        max_len = 0
        seen = set()

        while right < n:
            if s[right] not in seen:
                seen.add(s[right])
                window_len = right - left + 1

                if window_len > max_len:
                    max_len = window_len
                right += 1
            else:
                seen.remove(s[left])
                left += 1
        return max_len


        
        
        