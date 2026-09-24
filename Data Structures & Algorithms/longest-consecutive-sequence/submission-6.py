class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        hashset = set(nums)
        max_length = 0
        
        for num in hashset:
            if (num-1) not in hashset:
                length = 1
                current = num
                while (current+1) in hashset:
                    length +=1
                    current +=1
                max_length = max(max_length,length)
                length = 1
        
        return max_length
            
        
