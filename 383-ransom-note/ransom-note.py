class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for index,value in enumerate(ransomNote):
            dic[value] = ransomNote.count(value)
        print(dic) 

        dic1 = {}
        for index,value in enumerate(magazine):
            dic1[value] = magazine.count(value)
        print(dic1)          

        for index,key in enumerate(dic):
            if key not in dic1 or dic[key] > dic1[key]:
                return False
        return True        
        
          
