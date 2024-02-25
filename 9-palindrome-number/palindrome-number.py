class Solution:
    def isPalindrome(self, x: int) -> bool:
        print(x)
        x  = str(x)
        print(x)
        reversed = x[::-1]
        print(reversed)
        if reversed == x:
            return True
        else:
            return False    
    