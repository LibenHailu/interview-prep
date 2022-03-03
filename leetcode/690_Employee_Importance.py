"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        max_importance = 0

        stack = []

        for emp in employees:
            if emp.id == id:
                stack.append(emp)

        while stack:

            node = stack.pop()

            max_importance += node.importance

            for n in node.subordinates:
                for emp in employees:
                    if n == emp.id:
                        stack.append(emp)

        return max_importance
