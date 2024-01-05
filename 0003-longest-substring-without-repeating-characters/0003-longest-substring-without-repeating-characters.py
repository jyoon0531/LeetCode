class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        str_dic = {}

        lt = 0

        for i, x in enumerate(s, lt):
            if x in str_dic and lt <= str_dic[x]:
                lt = str_dic[x] + 1
            else: 
                maxLen = max(maxLen, i - lt + 1)
            str_dic[x] = i

        return maxLen