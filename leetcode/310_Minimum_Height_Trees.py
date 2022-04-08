class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        if n < 3:
            return list(range(n))

        adj = defaultdict(set)
        unseen = n

        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        dq = deque([i for i in adj if len(adj[i]) == 1])

        while dq:
            len_ = len(dq)

            if len_ == unseen:
                return dq

            for _ in range(len_):
                leaf = dq.pop()

                while adj[leaf]:
                    parent = adj[leaf].pop()
                    adj[parent].remove(leaf)
                    unseen -= 1
                    if len(adj[parent]) == 1:
                        dq.appendleft(parent)
