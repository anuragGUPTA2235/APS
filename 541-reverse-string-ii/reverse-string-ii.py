class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        list = []
        left = 0
        for i in range(len(s)):
            if i % (2*k) == 0  :
                list.append(s[left:i])
                left = i
        list.append(s[left:])
        del(list[0])
        print(list)
        
        for i in range(len(list)):
            list[i] = list[i][:k][::-1] + list[i][k:]
        print(list)  




        return "".join(list)      
        