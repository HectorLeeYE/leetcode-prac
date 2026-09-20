import operator
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        dict = {}

        for num in nums:
            dict[num] = dict.get(num,0) + 1
        sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)

        return [item[0] for item in sorted_dict[:k]]