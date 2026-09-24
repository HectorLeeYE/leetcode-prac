class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) > 0:
            length = 1
            max_length = 0
        else:
            return 0
        hashset = set(nums)
        
        start_num = 0
        for num in hashset:
            if (num-1) not in hashset:
                start_num = num
                while (start_num+1) in hashset:
                    length +=1
                    start_num +=1
                max_length = max(max_length,length)
                length = 1
        
        return max_length