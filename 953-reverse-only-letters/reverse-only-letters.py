class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        listt = []
        for items in s:
            if items.isalpha():
                listt.append(items)

        listt[::] = listt[::][::-1]
        tracker = 0 
        for idex,items in enumerate(s):
            if items.isalpha():
                s[idex] = listt[tracker]   
                tracker += 1


        return "".join(s)             



