class Solution:
    def changeToMin(self, s: str) -> int:
        h,m = s.split(":")
        h,m = int(h),int(m)
        return h * 60 + m 
    
    def findMinDifference(self, timePoints: List[str]) -> int:
        for i in range(len(timePoints)):
            timePoints[i] = self.changeToMin(timePoints[i]) 
            
        timePoints.sort()
        ans = sys.maxsize
        for i in range(1,len(timePoints)):
                ans = min(ans, timePoints[i] - timePoints[i - 1])
        
        ans = min(ans, 24 * 60 - timePoints[-1] + timePoints[0])
        return ans