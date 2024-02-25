class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        res  = []
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                sub = s[i:j]
                res.append(sub)
        #print(res) 
        for i in range(len(res)):
            unique = set(res[i])
            unilist = []
            for items in unique:
                unilist.append(items)
            unilist.sort()    
            check = sorted(res[i]) 
            if unilist != check:
                res[i] = "none"
        #print(res)        

        maximus = 0
        for items in res:
           if len(items) > maximus and items!="none":
               maximus = len(items)
        return maximus   
        """   
        maximus = 0   
        uni = []
        left = 0
        maxlength  = 0
        right= 0
        while right != len(s):
            if s[right] not in uni:
                uni.append(s[right])
                maximus += 1
                maxlength = max(maximus,maxlength)
                right += 1
            else:
                left = left + 1
                uni = []
                maximus = 0
                right = left


        print(uni)           
        return maxlength     

        