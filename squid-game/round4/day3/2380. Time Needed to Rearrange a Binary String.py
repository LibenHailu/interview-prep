class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        zeros = seconds = 0
        for i in s:
            if i == "0":
                zeros += 1
            elif zeros > 0:
                seconds = max(zeros,seconds + 1)
        return seconds