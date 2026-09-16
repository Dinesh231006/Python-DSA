"""Running Range
Problem Statement
Given an array of daily measurements, after each day calculate:
maximum value seen so far - minimum value seen so far
Example
Input:
5
10 5 15 8 20
Running maximum:
10 10 15 15 20
Running minimum:
10 5 5 5 5
Range:
0 5 10 10 15
Input Format
N
A1 A2 ... AN
Output Format
Print the running range after every element.
Constraints
1 ≤ N ≤ 100000
-10^9 ≤ Ai ≤ 10^9
Test Cases
#	Input	                        Output
1	5 / 10 5 15 8 20	      0 5 10 10 15
2	4 / 5 5 5 5	              0 0 0 0
3	5 / 1 2 3 4 5	              0 1 2 3 4
4	5 / 10 8 6 4 2	      0 2 4 6 8
5	5 / -5 0 -10 10 5	      0 5 5 20 20"""
arr=list(map(int,input().split()))
a=arr[0]
b=arr[0]
big=[]
small=[]
output=[]
for i in range(len(arr)):
    if arr[i]>a:
        a=arr[i]
    big.append(a)    

for i in range(len(arr)):
    if arr[i]<b:
        b=arr[i]
    small.append(b)    
for i in range(len(arr)):
    output.append(big[i]-small[i])
print(*output)
