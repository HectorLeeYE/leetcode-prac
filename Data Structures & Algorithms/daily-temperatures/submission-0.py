class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [0] * (len(temperatures))        # Last is always 0
        stack = [] 

        for i in range((len(temperatures)-1),-1,-1):        # Parse entire list backwards
            while stack and (temperatures[stack[-1]] <= temperatures[i]):
                stack.pop()
            if stack:
                arr[i] = stack[-1] -i
            stack.append(i)

        return arr

                
                
