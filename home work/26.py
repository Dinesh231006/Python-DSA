"""Given an integer array arr[] and a number k. Find the count of distinct elements in every window of size k in the array.

Examples:

Input: arr[] = [1, 2, 1, 3, 4, 2, 3], k = 4
Output: [3, 4, 4, 3]
Explanation:
First window is [1, 2, 1, 3], count of distinct numbers is 3.
Second window is [2, 1, 3, 4] count of distinct numbers is 4.
Third window is [1, 3, 4, 2] count of distinct numbers is 4.
Fourth window is [3, 4, 2, 3] count of distinct numbers is 3."""

from collections import deque

class Solution:
    def countDistinct(self, arr, k):
        freq = {}
        window = deque()
        output = []

        for i in range(len(arr)):
            window.append(arr[i])
            freq[arr[i]] = freq.get(arr[i], 0) + 1

            if len(window) > k:
                removed = window.popleft()
                freq[removed] -= 1
                if freq[removed] == 0:
                    del freq[removed]
            if len(window) == k:
                output.append(len(freq))

        return output