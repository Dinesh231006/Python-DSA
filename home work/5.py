"""You are given an array of integers arr[]. You have to reverse the given array.
Note: Modify the array in place."""
class Solution:
    def reverseArray(self, arr):
        for i in range(1,len(arr)//2+1):
            arr[i-1],arr[-i]=arr[-i],arr[i-1]
        return(arr)    
            
        