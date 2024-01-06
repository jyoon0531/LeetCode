import heapq

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
        
        i = heapq.nlargest(2, heap)[0]-1
        j = heapq.nlargest(2, heap)[1]-1

        return i*j
        