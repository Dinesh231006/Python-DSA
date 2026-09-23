"""Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.

 

Example 1:

Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).
"""

class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        output=0
        sub=sum(arr[:k])
        if (sub/k)>=threshold:
            output+=1
        for i in range(len(arr)-k):
            sub-=arr[i]
            sub+=arr[k+i]
            if (sub/k) >= threshold:
                output+=1
        return output