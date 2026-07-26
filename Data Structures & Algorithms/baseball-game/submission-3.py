class Solution:
    def calPoints(self, operations: List[str]) -> int:
        if len(operations) == 0:
            return None
        
        sum = 0
        new_arr = []
        
        for i in range(len(operations)):
            value = operations[i]
            print("Value: ", value)

            try:
                value = int(value)
            except (ValueError, AttributeError):
                # It's A Letter
                if value == "C":
                    val = new_arr.pop()
                    print("Popped: ", val)
                elif value == "D":
                    val = new_arr.pop()
                    new_score = val * 2
                    new_arr.append(val)
                    new_arr.append(new_score)
                elif value == "+":
                    val = new_arr.pop()
                    val_2 = new_arr.pop()
                    new_val = val + val_2
                    new_arr.append(val_2)
                    new_arr.append(val)
                    new_arr.append(new_val)
            else:
                # It's a number
                print("Appended: ", value)
                new_arr.append(value)
        
            print("return array: ", new_arr)

        for i in range(len(new_arr)):
            sum += new_arr[i]
        
        return sum
