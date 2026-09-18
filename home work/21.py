"""You are given an array arr of size n and an integer k. Your task is to find a pair of integers in the array such that it follows two conditions:
The sum of the pair is the maximum possible but less than k.
Out of all such pairs, choose the one with the maximum absolute difference between the two integers.
If no such pair exists, return (-1, -1).
Example:
Input: arr = [2, 4, 3, 6, 8, 10], k = 10
Output: (3, 6)
Explanation:
The pair (3, 6) has a sum of 9, which is less than 10. Among all pairs with sums less than 10, (3, 6) has the maximum absolute difference."""

class Solution:
    def maxSum(self, arr, k):
        arr.sort()
        a = 0
        b = len(arr) - 1

        max_sum = -1
        max_diff = -1
        ans = (-1, -1)

        while a < b:
            s = arr[a] + arr[b]

            if s >= k:
                b -= 1
            else:
                diff = arr[b] - arr[a]
                if s > max_sum or (s == max_sum and diff > max_diff):
                    max_sum = s
                    max_diff = diff
                    ans = (arr[a], arr[b])
                a += 1

        return ans