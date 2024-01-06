import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []

        soldierlist = []
        
        for i, m in enumerate(mat):
            cnt = 0
            for el in m:
                if el == 1:
                    cnt += 1
            soldierlist.append((cnt, i))
        

        for s in soldierlist:
            heapq.heappush(heap, s)
        
        answer = []

        weakrows = heapq.nsmallest(k, heap)

        for w in weakrows:
            answer.append(w[1])
        
        return answer
        


        