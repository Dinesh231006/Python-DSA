"""Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
Example 1:
Input: s = "leetcode"
Output: 0"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in range(len(s)):
            pop=s[i]
            st=s[:i]+s[i+1:]
            if pop not in st:
                return i
        return -1