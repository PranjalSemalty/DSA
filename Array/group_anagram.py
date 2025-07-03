# https://neetcode.io/problems/anagram-groups?list=neetcode250
# NeetCode 250 - Arrays & Hashing
# Difficulty: Medium

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())