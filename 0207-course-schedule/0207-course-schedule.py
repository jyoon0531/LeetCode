class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 각 수업에 대한 선행 과목들로 그래프 만들기
        graph = {i: [] for i in range(numCourses)}
        for prerequisite in prerequisites:
            graph[prerequisite[0]].append(prerequisite[1])
        

        traced = set()
        visited = set()

        def dfs(course):
            if course in traced:
                return False
            if course in visited:
                return True

            traced.add(course)

            for prerequisite in graph[course]:
                if not dfs(prerequisite):
                    return False
            
            traced.remove(course)
            visited.add(course)

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True