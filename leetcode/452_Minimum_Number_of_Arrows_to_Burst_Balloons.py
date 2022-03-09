class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
    
        if not points:
            return 0
        
        count = 1
        curEnd = points[0][1]
        print(curEnd)
        for i in range(1,len(points)):
            if points[i][0] > curEnd:
                count+=1
                curEnd = points[i][1]
                
        
        return count