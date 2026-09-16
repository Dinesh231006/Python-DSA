"""Given an array arr[], check whether it is sorted in non-decreasing order. Return true if it is sorted otherwise false.

Examples:

Input: arr[] = [10, 20, 30, 40, 50]
Output: true"""

class Solution:
    def isSorted(self, arr):
        for i in range(len(arr)-1):
            if arr[i]<=arr[i+1]:
                continue
            return False
        return True