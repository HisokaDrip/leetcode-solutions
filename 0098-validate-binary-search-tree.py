# 98. Validate Binary Search Tree (Medium)
# https://leetcode.com/problems/validate-binary-search-tree/
# Approach: DFS carrying an exclusive (low, high) bound for every node.
# Time: O(n), Space: O(h)
from typing import Optional


class Solution:
    def isValidBST(self, root: Optional["TreeNode"]) -> bool:
        def check(node, lo, hi):
            if not node:
                return True
            if not (lo < node.val < hi):
                return False
            return check(node.left, lo, node.val) and check(node.right, node.val, hi)

        return check(root, float("-inf"), float("inf"))
