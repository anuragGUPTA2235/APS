class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

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

        