class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # visited 배열 인덱스는 행, 값은 열	-> visited[row] = col 여기에 퀸이 놓여있다
        visited = [-1] * n 
        cnt = 0
        answer = []
        
        # is_ok_on(nth_row) -> n번째 행에 퀸을 놓을 수 있는지 판단
        def is_ok_on(nth_row: int) -> bool:
            for row in range(nth_row):
                # 같은 열에 퀸 두면 안되고, 대각선 방향도 안됨 -> return False로 처리
                if visited[nth_row] == visited[row] or nth_row - row == abs(visited[nth_row] - visited[row]):
                    return False

            return True
        # dfs(row) -> n번 행에 퀸 놓기
        def dfs(row):
            if row >= n:
                grid = [['.'] * n for _ in range(n)]
                nonlocal cnt
                cnt += 1
                for idx, val in enumerate(visited):
                    grid[idx][val] = 'Q'
                result = []
                for row in grid:
                    result.append(''.join(row))
                answer.append(result)
                return

            for col in range(n):
                visited[row] = col
                if is_ok_on(row):
                    dfs(row + 1)
        
        dfs(0)
        return answer
