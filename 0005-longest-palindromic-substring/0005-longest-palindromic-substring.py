class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(lt, rt: int) -> str:
            while lt >= 0 and rt < len(s) and s[lt] == s[rt]:
                lt -= 1
                rt += 1
            return s[lt+1:rt]
        
        maxStr = ''
        for i in range(len(s)):
            oddS = expand(i, i)
            if len(oddS) > len(maxStr):
                maxStr = oddS
            evenS = expand(i, i+1)
            if len(evenS) > len(maxStr):
                maxStr = evenS

        return maxStr    
    