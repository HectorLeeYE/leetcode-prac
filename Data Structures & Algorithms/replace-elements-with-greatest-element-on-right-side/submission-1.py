class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        new_max = arr[len(arr)-1]
        arr[len(arr)-1] = -1
        for i in range( (len(arr)-2), -1, -1):  # start from back, stop at 0, decrement by -1 every time
            old_value = arr[i]
            arr[i] = new_max

            if old_value > new_max:
                new_max = old_value
            
            

        return arr