class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_arr = []
        new_arr2 = []

        for num in nums:
            new_arr.append(num)
            new_arr2.append(num)
    
        return (new_arr+new_arr2)