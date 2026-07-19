class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = 0
        max_count = 0

        for number in nums:
            # If number is 1, increment count
            if number == 1:
                count += 1
            else:
                # Check whether this count is greater or lesser than max_count
                # if (count > max_count):
                #     max_count = count
                # else:
                #     # count lesser than max_count, can ignore
                #     print("ignore")
                # count = 0
                max_count = max(max_count,count)
                count = 0

        # A final check if the final number is 1
        return max(max_count,count)