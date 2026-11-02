# 15. 3Sum (Medium)
# https://leetcode.com/problems/3sum/
# Approach: sort, fix one element, then two pointers on the rest; skip
#           duplicates to keep triplets unique.
# Time: O(n^2)  Space: O(1) extra (excluding output and sort)
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                t = nums[i] + nums[l] + nums[r]
                if t < 0:
                    l += 1
                elif t > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
