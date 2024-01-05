class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        stones_dictionary = {}

        for stone in stones:
            stones_dictionary[stone] = stones_dictionary.get(stone, 0) +1

        for jewel in jewels:
            if jewel in stones_dictionary:
                cnt += stones_dictionary[jewel]

        return cnt        
