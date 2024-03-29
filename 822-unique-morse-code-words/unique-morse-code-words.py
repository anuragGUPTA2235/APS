class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        res = []

        hashmap = {}
        for index,items in enumerate(alpha):
            hashmap[items] = morse[index]


        for items in words:
            code = ""
            for jtems in items:
                code = code +  hashmap[jtems]
            res.append(code)       

        uni = set() 
        for items in res:
            uni.add(items)   

        print(hashmap)
        print(res)
        print(uni)


        return len(uni)


        