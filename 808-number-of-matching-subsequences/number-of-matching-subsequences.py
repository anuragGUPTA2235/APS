class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        """
        count = 0
        for items in words:
            
            p1 = 0
            p2 = 0
            while p1 < len(s) and p2 < len(items):
                if s[p1] == items[p2]:
                    p2 += 1
                p1 += 1
            if p2 == len(items):
                count += 1
        return count  
        """          

        count = 0
        for word in words:
            index = -1
            flag = 0
            for char in word:
                index = s.find(char,index+1)
                if index == -1:
                    flag = 1
                    break
            if flag == 0:        
             count += 1

        return count            

                

        
        return 7    

        