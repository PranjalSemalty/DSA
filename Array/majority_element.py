
# https://neetcode.io/problems/majority-element?list=neetcode250
# NeetCode 250 - Arrays & Hashing
# Difficulty: Easy

class Solution:
    def majorityElement(self, nums):
        count = {}
        res = maxCount = 0

        for num in nums:
            count[num] += 1
            if maxCount < count[num]:
                res = num
                maxCount = count[num]
        return res