"""Given a string s. The task is to find the first repeated character in it. We need to find the character that occurs more than once and whose index of second occurrence is smallest. s contains only lowercase letters.
Examples :
Input: s ="geeksforgeeks"
Output: "e""""
class Solution:
    def firstRepChar(self, s):
        # code here
        a=[]
        for i in range(len(s)):
            if s[i] in a:
                return s[i]
            a.append(s[i])
        return -1