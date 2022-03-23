from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        char_dict = {}
        result = []
        size = 0
        end = 0

        for i, v in enumerate(s):

            if not v in char_dict:
                char_dict[v] = i

            char_dict[v] = i

        for i, c in enumerate(s):

            size += 1
            if char_dict[c] > end:
                end = char_dict[c]

            if i == end:
                result.append(size)
                size = 0

        return result
