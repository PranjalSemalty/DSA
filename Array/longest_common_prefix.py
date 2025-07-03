# https://neetcode.io/problems/longest-common-prefix?list=neetcode250
# NeetCode 250 - Arrays & Hashing
# Difficulty: Easy

class Solution:
    def longestCommonPrefix(self, strs):
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i== len(s) or strs[0][i] != s[i]:
                    return res
            res += strs[0][i]
        return res 
