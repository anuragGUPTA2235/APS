class Solution:
    def minimumSum(self, num: int) -> int:

        list = []
        while num != 0:
            digit = num % 10
            list.append(digit)
            num  = num // 10
        print(list)
        list.sort(reverse = True)
        print(list)

        maxlist = list[:2]
        minlist = list[2:]
        print(maxlist)
        print(minlist)

        num1 = ""
        num2 = ""
        maxlist = [str(items) for items in maxlist]
        minlist = [str(items) for items in minlist]

        print(maxlist)
        print(minlist)

        num1 = num1 + minlist[0] + maxlist[0]
        num2 = num2 + minlist[1] + maxlist[1]

        num1 = int(num1)
        num2  = int(num2) 

        return num1 + num2