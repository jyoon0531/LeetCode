class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        store = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }

        result = []
        
        def dfs(L: int, strs: str):
            if len(digits) == 0:
                return result
            
            if len(digits) == L:
                result.append(strs)
                return
            
            for i in store[digits[L]]:
                dfs(L+1, strs+i)        
            # dfs(1, 'a') dfs(1, 'b') dfs(1, 'c')
            # dfs(2, 'ad') dfs(2, 'ae') dfs(2, 'af') ...
        
        dfs(0, '')

        return result
