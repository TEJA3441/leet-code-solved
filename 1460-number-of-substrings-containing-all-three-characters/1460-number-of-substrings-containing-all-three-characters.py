class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        l = 0
        count = 0
        mapp = {"a": 0, "b": 0, "c": 0}

        for r in range(n):
            mapp[s[r]] += 1

            while mapp["a"] > 0 and mapp["b"] > 0 and mapp["c"] > 0:
                count += (n - r)
                mapp[s[l]] -= 1
                l += 1

        return count
