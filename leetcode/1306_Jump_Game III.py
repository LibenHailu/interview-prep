class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        q = deque([(start, arr[start])])

        isVisited = set()
        isVisited.add(start)

        while q:

            start, val = q.popleft()

            if val == 0:
                return True

            if start + val < len(arr) and (start + val) not in isVisited:
                q.append((start + val, arr[start+val]))
                isVisited.add(start + val)

            if start - val >= 0 and (start - val) not in isVisited:
                q.append((start - val, arr[start - val]))
                isVisited.add(start - val)

        return False
