class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = []

        for token in tokens:
            if token not in {'+','-','*','/'}:      # it's a number
                arr.append(int(token))
            else:
                right_val = arr.pop()
                left_val = arr.pop()
                
                if token == '+':
                    result = left_val + right_val
                elif token == '-':
                    result = left_val - right_val
                elif token == '*':
                    result = left_val * right_val
                elif token == '/':
                    result = int(left_val / right_val)
                
                arr.append(result)
        
        return arr[0]