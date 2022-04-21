class Solution:

    def __init__(self, n):
        self.pars = [i for i in range(1, n+1)]
        self.ranks = [1]*n

    def find(self, n1):
        if n1 != self.pars[n1 - 1]:
            n1 = self.pars[n1 - 1] = self.pars[self.pars[n1 - 1]]
            # return n1

        return n1

    def union(self, n1, n2):
        r1, r2 = self.find(n1), self.find(n2)

        if r1 == r2:
            return False

        if self.ranks[r1 - 1] > self.ranks[r2 - 1]:
            self.pars[r2 - 1] = r1
        elif self.ranks[r2 - 1] > self.ranks[r1 - 1]:
            self.pars[r1 - 1] = r2
        else:
            self.pars[r2 - 1] = r1
            self.ranks[r1 - 1] += 1

    def memQuery(self, n1):
        root = self.pars[n1 - 1]
        count = 0
        for i in self.pars:
            if i == root:
                count += 1

        return count


if __name__ == "__main__":
    # query = input()
    inputs = list(map(int, input().split()))
    m = Solution(inputs[0])
    for i in range(inputs[1]):
        q = list(input().split())
        if q[0] == 'Q':
            print(m.memQuery(int(q[1])))
        else:
            m.union(int(q[1]), int(q[2]))
            print(m.memQuery(int(q[1])))
