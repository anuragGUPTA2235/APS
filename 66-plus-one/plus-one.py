class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        print(digits)
        i = len(digits)
        for _ in range(i-1,-1,-1):
            if digits[_] != 9:
                print("hello")
                digits[_]+=1
                return digits
            digits[_] = 0
        print("jhh",digits)    
        return [1] + digits    

     
     
        

        