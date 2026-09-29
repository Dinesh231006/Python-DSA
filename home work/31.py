"""Given a string s, consisting of lowercase alphabets. Remove consecutive duplicate characters from the string. 

Example:

Input: s = "aabb"
Output: "ab" 
Explanation: The character 'a' at index 2 is the same as 'a' at index 1, so it is removed.Similarly, the character 'b' at index 4 is the same as 'b' at index 3, so it is removed. The final string is "ab".
Input: s = "aabaa"
Output: "aba"
Explanation: The character 'a' at index 2 is the same as 'a' at index 1, so it is removed. The character 'a' at index 5 is the same as 'a' at index 4, so it is removed. The final string is "aba".
Input: s = "aaaa"
Output: "a"
Explanation: "aaaa" => "aaa" => "aa" => "a" """

class Solution:
    def removeDuplicates(self, s):
        a=[s[0]]
        
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                continue
            a.append(s[i])
        return "".join(a)