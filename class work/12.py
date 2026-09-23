"""Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
Example 1:
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1"""

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l=0
        tem=0
        min_l=float('inf')
        for r in range(len(nums)):
            tem+=nums[r]
            while tem >=target:
                min_l=min(min_l,r-l+1)
                tem-=nums[l]
                l+=1

        return min_l if min_l != float("inf") else 0 
        