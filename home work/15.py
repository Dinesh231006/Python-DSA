"""You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

Return the sum of all the unique elements of nums.

Example 1:
Input: nums = [1,2,3,2]
Output: 4"""

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        a={}
        for i in nums:
            a[i]=a.get(i,0)+1
        b=[key for key,value in a.items() if value ==1]
        return sum(b)