class Solution:
    def isValid(self, s: str) -> bool:
        input = list(s)
        new_arr = []

        if len(input) == 0:
            return False
        elif len(input) % 2 != 0:
            return False

        for i in range(len(input)):
            # read the first element and push into a stack if opening
            first_element = input[i]
            print("First Element: ", first_element)

            if (first_element == "(" or first_element == "{" or first_element == "["):
                new_arr.append(first_element)
            else: 
                # Closing bracket so pop the new_arr and compare immediately
                if len(new_arr) == 0:
                    return False
                element = new_arr.pop()
                sum_element = element + first_element
                print("Sum Element: ", sum_element)
                if (sum_element == "()" or sum_element == "{}" or sum_element == "[]"):
                    continue
                else:
                    return False

        if len(new_arr) > 0:
            return False

        return True



        
