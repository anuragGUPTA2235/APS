class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # brute force
        count = 0
        for items in grid:
            for jtems in items:
                if jtems < 0:
                 count += 1
        return count        
        