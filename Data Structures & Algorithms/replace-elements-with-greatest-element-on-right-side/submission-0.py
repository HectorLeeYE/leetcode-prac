class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        start_max = -1

        for i in range(len(arr)-1, -1, -1):
            new_max = max(start_max, arr[i])
            arr[i] = start_max
            start_max = new_max


        return arr