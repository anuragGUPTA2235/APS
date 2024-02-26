class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        uni = list(set(nums))
        print(uni)

        dic = {}
        for items in uni:
            dic[items] = 0
        print(dic)    
        for items in nums:
            dic[items] +=1
        print(dic)    

        maxval = max(dic,key = dic.get)

        return  maxval
        