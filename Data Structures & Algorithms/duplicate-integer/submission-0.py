class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        dict = {}

        for num in nums:
            if num not in dict.keys():
                dict[num] = True
            else:
                return True
        
        return False 