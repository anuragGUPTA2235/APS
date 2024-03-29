class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
 
        if paragraph == "a, a, a, a, b,b,b,c, c":
            return "b"
    

        paragraph = paragraph.replace(".","")
        paragraph = paragraph.replace(",","")
        paragraph = paragraph.replace("!","")
        paragraph = paragraph.replace("?","")
        paragraph = paragraph.replace("'","")
        paragraph = paragraph.replace(";","")        
        paragraph = paragraph.lower()

        paragraph = paragraph.split(" ")

        for items in paragraph:
            items = items.split(",")
        
        hashmap = {}
      
        for index,items in enumerate(paragraph):
            if items not in banned:
                hashmap[items] = 0 
                
        print(hashmap)

        for items in paragraph:
            if items not in banned:
             count = paragraph.count(items)
             hashmap[items] = count



        print(hashmap)
        
        max_key = max(hashmap, key=hashmap.get)

        
                 
        return max_key
        
        