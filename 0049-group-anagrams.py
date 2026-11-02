# 49. Group Anagrams (Medium)
# https://leetcode.com/problems/group-anagrams/
# Approach: use the sorted characters of each word as a hash key.
# Time: O(n * k log k), Space: O(n * k)
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            key = tuple(sorted(s))
            groups.setdefault(key, []).append(s)
        return list(groups.values())
