class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix = strs[0]  # Take the first word as a starting prefix
        
        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]  # Remove last character until match
                if not prefix:
                    return ""
        
        return prefix
