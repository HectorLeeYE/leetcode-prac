class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        arr_1 = [0] * 26
        arr_2 = [0] * 26        # Works because both are same len

        for i in range(len(s)):

            position_1 = ord(s[i]) % 26
            position_2 = ord(t[i]) % 26

            arr_1[position_1] = (arr_1[position_1]+1)
            arr_2[position_2] = (arr_2[position_2]+1)

        if arr_1 != arr_2:
            return False
        else:
            return True