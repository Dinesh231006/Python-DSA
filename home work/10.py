"""Given an array arr[] with indices ranging from 0 to arr.size() - 1, rearrange the elements so that the value at each index i becomes i. If the value i is not present in the array, place -1 at index i.

Note: The array does not contain any duplicate non-negative values.

Examples:

Input: arr[] = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
Output: [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]"""

class Solution:
    def modifyArray(self, arr):
        s = set(arr)
        for i in range(len(arr)):
            if i in s:
                arr[i] = i
            else:
                arr[i] = -1
        return arr