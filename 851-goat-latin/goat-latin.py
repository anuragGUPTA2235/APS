class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sen = sentence.split(" ")
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        print(sen)
        for i in range(len(sen)):
            print(sen[i])
            if sen[i][0] in vowels:
                sen[i] += 'ma' 
            elif sen[i][0] not in vowels:




                temp = sen[i][0]
                sen[i] = sen[i][1:]
                sen[i] += temp
                sen[i] += 'ma' 

            sen[i] += 'a' * (i+1) 
            print(sen[i])   

        res = ""
        for i in range(len(sen)-1):
            res = res + sen[i] + " "    

        res = res + sen[-1]
        return res


