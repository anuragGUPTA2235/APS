class Solution:
    def reverseWords(self, s: str) -> str:
        """

        s = s.split(" ")
        res = ""
        print(s)

        for i in range(len(s)-1):
            s[i] = s[i][::-1] 
            res = res + s[i] + " "


        return res + s[-1][::-1]
        """

        left = 0 
        s = list(s)

        for right,items in enumerate(s):
            if s[right] == " ":
                s[left:right] = s[left:right][::-1]
                left = right + 1

        s[left:] = s[left:][::-1]        
        return "".join(s)    


        