# 56. Merge Intervals (Medium)
# https://leetcode.com/problems/merge-intervals/
# Approach: sort by start, then merge each interval into the last one if they overlap.
# Time: O(n log n)  Space: O(n)
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        out = [intervals[0]]
        for s, e in intervals[1:]:
            if s <= out[-1][1]:
                out[-1][1] = max(out[-1][1], e)
            else:
                out.append([s, e])
        return out
