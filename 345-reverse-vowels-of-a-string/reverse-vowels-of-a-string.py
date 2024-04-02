class Solution:
    def reverseVowels(self, s: str) -> str:
        
        """
    
        listt = ['a','e','i','o','u','A','E','I','O','U']
        vowels = []
    
        for i in range(len(s)):
            if s[i] in listt:
                vowels.append(s[i])
        #vowels[::] = vowels[::-1]


        j = len(vowels) - 1

        for i  in range(len(s)):
            if s[i] in vowels:
                s[i].replace(s[i],vowels[j])
                j -= 1
                

     

        return "".join(s)    
        """

        left = 0
        right = len(s) - 1
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        s = list(s)

        while left < right:

            while s[left] not in vowels and left < len(s)-1:
                left += 1
            while s[right] not in vowels and right>= 0:
                right -= 1

            if left < right:   

             s[left],s[right] = s[right],s[left]
            
            left += 1
            
            right -= 1 
            
            

        return "".join(s)    
        

        