"""Given an array of non-negative integers. Your task is to rearrange the array elements alternatively i.e. first element should be the max value, the second should be the min value, the third should be the second max, the fourth should be the second min, and so on.
Note: Modify the original array itself. You do not have to return anything."""

class Solution:
    def rearrange(self, arr):
        arr.sort()
        for i in range(1,len(arr),2):
            a=arr.pop(-1)
            arr.insert(i-1,a)