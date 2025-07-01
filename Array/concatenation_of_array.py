# https://neetcode.io/problems/concatenation-of-array?list=neetcode250
# NeetCode 250 - Arrays & Hashing
# Difficulty: Easy

class Solution:
    def getConcatenation(self, nums):
        n = len(nums)
        ans = [0] * (2 * n)
        for i in range(n):
            ans[i]=nums[i]
            ans[i+n]=nums[i]
        return ans
