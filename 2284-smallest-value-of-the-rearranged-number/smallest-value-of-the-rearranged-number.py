class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 0:
            num = str(num)
            list = [int(items) for items in num[1:]]
            print(list)
            list.sort()
            list.sort(reverse = True)
            print(list)
            list = [str(items) for items in list]
            res = "-"
            for items in list:
                res = res + items 
            return int(res)

        elif num == 0:
            return 0

        elif num > 0:
            num = str(num)
            list = [int(items) for items in num]
            list.sort()
            print(list)  
            if list[0] == 0:
             for index,items in enumerate(list):
                if items != 0:
                    print(items)
                    list[0],list[index] = list[index],list[0]
                    break
             res = ""
             for items in list:
                res += str(items)
             print("hello")   
             return int(res)          
            else:
                res = ""
                for items in list:
                    res = res + str(items)
                return int(res)   




            

