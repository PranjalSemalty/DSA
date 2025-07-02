# https://neetcode.io/problems/is-anagram?list=neetcode250
# NeetCode 250 - Arrays & Hashing
# Difficulty: Easy

class Solution:
    def isAnagram(self,s,t):
        if len(s) != len(t):
            return False
            
        return sorted(s) == sorted(t)