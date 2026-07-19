class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 1) Change array such that first k elements contains the non-equal val
        # 2) Return k 

        non_equal_count = 0 

        for i in range(len(nums)):
            if val != nums[i]:
                # NOT Equal, so perform an inplace swap
                nums[non_equal_count] = nums[i]
                non_equal_count += 1

        return non_equal_count