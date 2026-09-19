class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for s in strs:
            arr_1 = [0] * 26

            for char in s:
                arr_1[ord(char)-97] += 1

            key = tuple(arr_1)

            if key not in dict:
                dict[key] = []    
            dict[key].append(s)
            
        return list(dict.values())