from typing import List


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times

    def q(self, t: int) -> int:

        left = 0
        right = len(self.times) - 1
        best = 0

        while left < right:

            mid = left + (right - left)//2

            if t >= self.times[mid]:
                best = mid
                left = mid + 1

            # elif t > self.times[mid]:
            #     best = mid
            #     left = mid + 1

            else:

                right = mid

        return self.persons[best]


# ["TopVotedCandidate", "q", "q", "q", "q", "q", "q", "q", "q", "q", "q"]
# [[[0, 0, 1, 1, 2], [0, 67, 69, 74, 87]], [4], [62],
#     [100], [88], [70], [73], [22], [75], [29], [10]]

# ["TopVotedCandidate","q","q","q","q","q","q"]
# [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
if __name__ == "__main__":
    obj = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30])
    print(obj.q(3))
    print(obj.q(12))
    print(obj.q(25))
    print(obj.q(15))
    print(obj.q(24))
    print(obj.q(8))
    # obj = TopVotedCandidate([0, 0, 1, 1, 2], [0, 67, 69, 74, 87])
    # # param_1 = obj.q(25)
    # # print(obj.q(4))
    # # print(obj.q(62))
    # # print(obj.q(100))
    # # print(obj.q(88))
    # print(obj.q(70))
    # print(obj.q(73))
    # print(obj.q(22))
    # print(obj.q(75))
    # print(obj.q(29))
    # print(obj.q(10))
    # print(param_1)
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
