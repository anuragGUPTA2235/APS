class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = ""
        for items in s:
            if items.isalnum():
                res = res + items
        rev = res[::-1]
        print(res)
        print(rev)
        if rev == res:
            return True
        else:
            return False 
  
        