class Solution:
    from collections import defaultdict
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            arr_1 = [0] * 26

            for char in s:
                arr_1[ord(char)-97] += 1
            ans[tuple(arr_1)].append(s)
            
            
        return list(ans.values())