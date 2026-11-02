# 3. Longest Substring Without Repeating Characters (Medium)
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Approach: sliding window with a last-seen index map; move the left edge past
#           the previous occurrence of a repeated character.
# Time: O(n)  Space: O(min(n, alphabet))


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last, left, best = {}, 0, 0
        for i, c in enumerate(s):
            if c in last and last[c] >= left:
                left = last[c] + 1
            last[c] = i
            best = max(best, i - left + 1)
        return best
