class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        print(matrix)
        rows = len(matrix[0])
        columns = len(matrix[0])
        for i in range((rows)):
            for j in range((columns)):
                if i > j:
                #print(matrix[i][j])
                 matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

        for rows in matrix:
            rows.reverse()         
                
        print(matrix)        

        