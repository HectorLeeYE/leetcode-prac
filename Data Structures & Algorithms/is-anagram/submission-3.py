class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        arr_1 = [0] * 26

        for i in range(len(s)):
            arr_1[ord(s[i]) - 97] += 1
            arr_1[ord(t[i]) - 97] -= 1

        if arr_1 == [0] * 26:
            return True
            
        return False