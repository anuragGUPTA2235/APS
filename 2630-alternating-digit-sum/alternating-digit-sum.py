class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)
        list = [int(items) for items in n]
        print(list)
        sum = 0
        for index,items in enumerate(list):
            if index % 2 == 0:
                sum += items
            else:
                sum -= items    



        return sum
        