class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        arr_1 = [0] * 26

        for c1,c2 in zip(s,t):
            arr_1[ord(c1) - 97] += 1
            arr_1[ord(c2) - 97] -= 1

        if arr_1 == [0] * 26:
            return True

        return False