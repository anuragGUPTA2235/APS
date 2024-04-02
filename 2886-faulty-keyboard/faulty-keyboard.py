class Solution:
    def finalString(self, s: str) -> str:
        res = ""
        s = list(s)

        for index,items in enumerate(s):
            if items == "i":
                a = list(res[::])
                a[::] = a[::][::-1]
                res = "".join(a)

            else:
                res += items   

        return res         
        