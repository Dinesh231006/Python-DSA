"""Given a square matrix mat, return the sum of the matrix diagonals.
Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.
Example 1:

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once."""

class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        a=0
        b=len(mat[0])-1
        s=0
        for i in mat:
            if a==b:
                s=s+i[a]
                a+=1
                b-=1
                continue
            s=s+i[a]+i[b]
            a+=1
            b-=1
        return s