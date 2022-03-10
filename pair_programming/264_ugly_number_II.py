import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        h = []
        vis = set()
        nth = 1
        heapq.heappush(h,1)
        
        while(nth <  n):
            mult = heapq.heappop(h)
            if mult * 2 not in vis:
                heapq.heappush(h,mult * 2)
                vis.add(mult*2)
            if mult * 3 not in vis:
                heapq.heappush(h,mult * 3)
                vis.add(mult*3)                                

            if mult * 5 not in vis:
                heapq.heappush(h,mult * 5)
                vis.add(mult*5)
            
            nth += 1
            
        return heapq.heappop(h)