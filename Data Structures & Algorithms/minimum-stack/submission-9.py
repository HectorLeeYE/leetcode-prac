class MinStack:

    def __init__(self):
        # Initialize an array to push and pop elements from 
        self.arr = []
        self.arr_2 = [] 

    def push(self, val: int) -> None:
        self.arr.append(val)
        # Set minimum element
        if len(self.arr_2) == 0:
            self.arr_2.append(val)
        # Push min val to the end
        else:
            self.arr_2.append(min(val,self.arr_2[-1]))      # Compare with last element, push smaller one inside 

    def pop(self) -> None:
        val = self.arr.pop()
        # When popping, check if it's the min_element
        self.arr_2.pop()


    def top(self) -> int:
        return self.arr[-1]
        #return top_element

    def getMin(self) -> int:
        return self.arr_2[-1]
        # print("Min Element: ", min_element)
        # return min_element