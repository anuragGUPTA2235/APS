class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
     for k in range(4):
      rows = len(mat)
      
      for i in range((rows)):
        for j in range((rows)):
            if i > j:
                mat[i][j],mat[j][i] = mat[j][i],mat[i][j]

      for row in mat:
            row.reverse() 
      if mat == target:
            return True
      print(mat)      
     return False                