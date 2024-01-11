class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = [False] * n
        answer = []

        def dfs(L):
            if L >= n:
                subset = []
                for idx, num in enumerate(nums):
                    if visited[idx]:
                        subset.append(num)
                answer.append(subset)
                return
            
            visited[L] = True
            dfs(L+1)
            visited[L] = False
            dfs(L+1)

        dfs(0)
        return answer