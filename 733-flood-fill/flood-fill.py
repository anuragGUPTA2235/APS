class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        print(len(image))
        print(len(image[0]))
    
        def dfs(image,sr,sc,color,source):
            if sr < 0 or sc < 0 or sr >= len(image) or sc >= (len(image[0])):
                return image
            elif image[sr][sc] == color:
                return image  
            elif image[sr][sc]!=source:
                return image     
            else:
             image[sr][sc] = color    

            dfs(image,sr-1,sc,color,source) # top
            dfs(image,sr+1,sc,color,source) # bottom
            dfs(image,sr,sc-1,color,source) # left
            dfs(image,sr,sc+1,color,source) # right

        source = image[sr][sc]
        dfs(image,sr,sc,color,source)
        
        return image    
        