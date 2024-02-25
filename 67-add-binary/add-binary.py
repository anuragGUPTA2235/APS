class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a,2)
        b = int(b,2)
        res = a+b
        print(a,b)
        print(res)
        res = bin(res)
        print(res)
        return res[2:]


        