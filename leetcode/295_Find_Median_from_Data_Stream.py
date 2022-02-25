from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        self.min_h = []
        self.max_h = []

    def addNum(self, num: int) -> None:

        if not self.min_h:
            heappush(self.min_h, num)

        elif len(self.min_h) > len(self.max_h):
            cur_mid = self.min_h[0]
            if num > cur_mid:
                heappush(self.max_h, -heappop(self.min_h))
                heappush(self.min_h, num)
            else:
                heappush(self.max_h, -num)

        elif len(self.min_h) == len(self.max_h):
            cur_mid = self.min_h[0]
            if num > cur_mid:
                heappush(self.min_h, num)
            else:
                heappush(self.max_h, -num)
        else:
            cur_mid = -self.max_h[0]
            if num < cur_mid:
                heappush(self.min_h, -heappop(self.max_h))
                heappush(self.max_h, -num)
            else:
                heappush(self.min_h, num)

    def findMedian(self) -> float:

        if len(self.min_h) > len(self.max_h):
            return self.min_h[0]

        elif len(self.min_h) < len(self.max_h):
            return -self.max_h[0]

        else:
            return (self.min_h[0] + -self.max_h[0]) / 2
