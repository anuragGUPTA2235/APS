class Solution:
    def longestPalindrome(self, s: str) -> str:
        #print(s)
     
        palin = []
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                sub = s[i:j]
                item = sub
                if item == item[::-1]:
                    palin.append(item)
        


        #print(palin)  
        max = 0
        for items in palin:
            if len(items) > max:
                max =len(items)
        #print(max)  
        for items in palin:
            if len(items) == max:
                return items           

        