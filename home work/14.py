"""Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears at most twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a={}
        for i in nums:
            a[i]=a.get(i,0)+1
        b=[key for key,value in a.items() if value == 2]
        return b