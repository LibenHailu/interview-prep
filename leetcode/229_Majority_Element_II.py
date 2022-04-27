class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = Counter(nums)
        res = []

        for c, v in count.items():
            if v > len(nums)/3:
                res.append(c)

        return res
