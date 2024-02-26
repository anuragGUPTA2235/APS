class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        print(s)
        s = s[::-1]
        print(s)
        res = ""
        for items in s:
            res = res + " " +  items

        print(res) 
        return res[1:]   

        