class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        occur = []
        for index,items in enumerate(s):
            if items == c:
                occur.append(index)
        ans = []
        p1 = 0
        for index,items in enumerate(s):
            if items == c:
                ans.append(0)
                p1 += 1
            elif index < occur[0]:
                dis = abs(occur[0]-index)
                ans.append(dis)
            elif index > occur[-1]:
                dis = index - occur[-1] 
                ans.append(dis)
            else:
                dis1 = abs(index - occur[p1])
                dis2 = abs(index - occur[p1-1]) 
                ans.append(min(dis1,dis2))

        return  ans              





        