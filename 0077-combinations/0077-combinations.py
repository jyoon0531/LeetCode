class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        cm = [0] * k

        def dfs(L, x):
            if L == k:
                result.append(cm[:])
            else:
                for i in range(x, n+1):
                    cm[L] = i
                    dfs(L+1, i+1)
        
        dfs(0, 1)

        return result