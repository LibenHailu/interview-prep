class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        counter = 0

        for row in grid:

            left = 0
            right = len(row)

            negative = {}

            while left < right:

                mid = (left + right) // 2

                if row[mid] > 0:
                    left = mid + 1

                elif row[mid] < 0:
                    right = mid - 1
                    if not negative:
                        negative['first_negative'] = 0

                    negative['first_negative'] = mid

            if negative:
                counter += len(row) - negative['first_negative']
                negative.pop('first_negative')

        return counter
