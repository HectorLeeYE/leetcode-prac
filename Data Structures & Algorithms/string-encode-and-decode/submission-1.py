class Solution:

    def encode(self, strs: List[str]) -> str:
        empty = ""

        for string in strs:
            empty = empty + str(len(string))+ "#" + string 

        return empty

    def decode(self, s: str) -> List[str]:
        arr = []
        i = 0
        while i < len(s):
            j = s.find('#',i)       # first occur of '#' is returned
            length = int(s[i:j])
            word = ""
            word += s[j+1:j+1+length]
            arr.append(word)
            i = (j+1+length)
        return arr

