class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams ={}
        
        for str in strs:
            # sorted를 활용하여 정렬한 str을 선언
            sortedStr = ''.join(sorted(str))
            
            # 정렬한 str을 key로 딕셔너리에 그룹 추가
            # 이미 해당 key가 있으면 그룹에 str 추가
            # 없으면 새로운 그룹 생성 
            if sortedStr in anagrams:
                anagrams[sortedStr].append(str)
            else:
                anagrams[sortedStr] = [str]

        result = list(anagrams.values())        

        return result