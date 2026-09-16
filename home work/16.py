"""Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

Example 1:
Input: arr = [1,2,2,1,1,3]
Output: true"""

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a={}
        for i in arr:
            a[i]=a.get(i,0)+1
        b=[value for key,value in a.items()]
        b.sort()
        for i in range(len(b)-1):
            if b[i]==b[i+1]:
                return False
        return True