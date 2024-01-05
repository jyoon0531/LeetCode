from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dic = {}

        for num in nums:
            nums_dic[num] = nums_dic.get(num, 0) + 1

        # value를 기준으로 내림차순 정렬 
        nums_dic = sorted(nums_dic.items(), key=lambda x: (-x[1], x[0]))

        answer = []
        
        for key, _ in nums_dic:
            if len(answer) < k:
                answer.append(key)
            elif len(answer) == k:
                break

        return answer
