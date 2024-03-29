
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxarea = -900
        for i in range(len(points)):
            for j in range(len(points)):
                for k in range(len(points)):
                    x1 = points[i][0]
                    x2 = points[j][0]
                    x3 = points[k][0]
                    y1 = points[i][1]
                    y2 = points[j][1]
                    y3 = points[k][1]
                    area = 0.5 * abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)))
                    print(area)
                    




                    print(area)
                    if area > maxarea:
                        maxarea = area 

        return maxarea