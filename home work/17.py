"""You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. Calculate the following values:

answer1 : the number of indices i such that nums1[i] exists in nums2.
answer2 : the number of indices i such that nums2[i] exists in nums1.
Return [answer1,answer2].
Example 1:
Input: nums1 = [2,3,2], nums2 = [1,2]
Output: [2,1]"""

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output=[]
        a={}
        for i in nums1:
            a[i]=a.get(i,0)+1
        b=sum([value for key,value in a.items() if key in nums2])
        a1={}
        for i in nums2:
            a1[i]=a1.get(i,0)+1
        b1=sum([value for key,value in a1.items() if key in nums1])
        return [b,b1]