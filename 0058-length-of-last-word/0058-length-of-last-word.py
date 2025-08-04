class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        n = len(s) - 1

        while n >= 0 and s[n] == " ":
            n -= 1

        answer = 0

        while n >= 0 and s[n] != " ":
            answer += 1
            n -= 1
        
        return answer
        

        
       
        