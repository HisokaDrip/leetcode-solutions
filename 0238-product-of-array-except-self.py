# 238. Product of Array Except Self (Medium)
# https://leetcode.com/problems/product-of-array-except-self/
# Approach: prefix products going left, then suffix products going right, no division.
# Time: O(n), Space: O(1) extra (output excluded)
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res
