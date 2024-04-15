class Solution:
    def isSameAfterReversals(self, num: int) -> bool:

        num = str(num)
        a = []
        for items in num:
            a.append(items)
        print(a)    
        c = a[::-1]
        print(c)

        tempnum = ""
        for items in c:
            tempnum += items
        tempnum = int(tempnum)
        tempnum = str(tempnum)
        z = []

        for items in tempnum:
            z.append(items)    
        b = z[::-1]  

        res = ""
        com = ""

        for items in a:
            res = res + items
        for items in b:
            com = com + items    
        print(res,com)    

        return int(res) == int(com)
        