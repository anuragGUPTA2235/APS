class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        v = sorted(strs)
        res = ""
     
        for i in range(min(len(v[0]),len(v[-1]))):
            if v[0][i] == v[-1][i]:
                res += v[0][i]

            else:
                break 
        print(res)  
        return res         

            

        
    
        