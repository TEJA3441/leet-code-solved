class Solution:
    def romanToInt(self, s: str) -> int:

        roman_map = {'I': 1,
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     'C': 100,
                     'D': 500,
                     'M': 1000}
        total = 0
        prev_val = 0

        for ch in reversed(s):
            value = roman_map[ch]
            if value < prev_val:
                total -= value
            else:
                total += value
                prev_val = value
        
        return total



        