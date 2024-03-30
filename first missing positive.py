from collections import Counter
class Solution(object):
    def firstMissingPositive(self, nums):
        c=Counter(nums)
        for i in range(len(nums)):
            if i+1 not in c:
                return i+1
        return len(nums)+1
