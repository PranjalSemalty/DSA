# https://neetcode.io/problems/duplicate-integer?list=neetcode250
# NeetCode 250 - Arrays & Hashing
# Difficulty: Easy

class Solution:
    def hasDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False