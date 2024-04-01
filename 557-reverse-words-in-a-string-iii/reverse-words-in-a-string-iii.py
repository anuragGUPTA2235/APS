class Solution:
    def reverseWords(self, s: str) -> str:


        s = s.split(" ")
        res = ""
        print(s)

        for i in range(len(s)-1):
            s[i] = s[i][::-1] 
            res = res + s[i] + " "


        return res + s[-1][::-1]
        