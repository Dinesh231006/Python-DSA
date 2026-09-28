"""Anagram
Given two non-empty strings s1 and s2, consisting only of lowercase English letters, determine whether they are anagrams of each other or not.
Two strings are considered anagrams if they contain the same characters with exactly the same frequencies, regardless of their order.

Examples:

Input: s1 = "geeks" s2 = "kseeg"
Output: true 
Explanation: Both the string have same characters with same frequency. So, they are anagrams.
Input: s1 = "allergy", s2 = "allergyy" 
Output: false 
Explanation: Although the characters are mostly the same, s2 contains an extra 'y' character. Since the frequency of characters differs, the strings are not anagrams. """

class Solution:
    def areAnagrams(self, s1, s2):
       # code here
        a={}
        for i in s1:
           a[i]=a.get(i,0)+1
        for i in s2:
            if i not in a:
                return False
            a[i]=a.get(i)-1
            if a[i] == 0:
                del a[i]
        return True