class Solution:
 def countNegatives(self, grid: List[List[int]]) -> int:
    # can use brute force also
      

             # efficient way
             """
             def bs_nested(nums):
                        countneg = 0
                
                        for i in range(len(grid)):
                             left = 0
                             right = len(grid[0])-1
                             while left <= right:
                               mid = (left + right) // 2
                            
                               if grid[i][mid] >= 0:
                                   left = mid + 1
                               else:
                                   right = mid - 1
                            
                               
                             countneg += (left) 
                             
    
                        return countneg     


             num = bs_nested(grid)
             return (len(grid*len(grid[0]))-num  )   
             """
             neg = 0
             for items in grid:
                for jtems in items :
                   if jtems < 0:
                    neg = neg +1
             return neg          


        

        