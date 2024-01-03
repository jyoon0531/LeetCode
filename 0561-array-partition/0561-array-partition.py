class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 합이 최대를 보장하기 위해 주어진 배열을 정렬 
        nums.sort()

        # 각 pair의 최소값들의 합
        result = sum(nums[i] for i in range(0, len(nums), 2))

        return result