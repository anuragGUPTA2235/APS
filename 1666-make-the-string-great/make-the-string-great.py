class Solution:
    def makeGood(self, s: str) -> str:

        
        res = s
        
        def checker(res):
            for index in range(len(res)-1):
                if ((res[index].isupper() and res[index+1].islower()) or (res[index].islower() and res[index+1].isupper())) and (res[index].lower() == res[index+1].lower()):
                    print("hello")
                    return 1
            return 0

        while checker(res):
         
    
         index = 0
         res = list(res)
         
         while index < (len(res)-1):
            if ((res[index].isupper() and res[index+1].islower()) or (res[index].islower() and res[index+1].isupper())) and (res[index].lower() == res[index+1].lower()):
              res[index],res[index+1] = "",""
              
            index += 1  

  

         res = "".join(res)
         print(res)
           
        return res      
        