class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        zeroSum = set()  

        nums.sort()  

        for i in range(len(nums) - 2):
            lt = i + 1 
            rt = len(nums) - 1

            while lt < rt:
                current_sum = nums[i] + nums[lt] + nums[rt]

                if current_sum == 0:
                    zeroSum.add((nums[i], nums[lt], nums[rt]))
                    lt += 1
                    rt -= 1
                elif current_sum < 0:
                    lt += 1
                else:
                    rt -= 1

        return list(zeroSum)
