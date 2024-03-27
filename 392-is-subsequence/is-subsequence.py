class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        pointer1 = 0
        length = 0
        if len(s) == 0:
            return True
        for i in range(len(t)):
            if t[i] == s[pointer1]:
                length += 1
                pointer1 += 1
                if pointer1 == len(s):
                    break
        print(length)  
        if length == len(s):
            return True 
        else:
            return False   
        """
        p1 = 0
        p2 = 0

        while p1 <len(s) and p2 < len(t):
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1             
        if p1 == len(s):
          return True
        else:
          return False 
        