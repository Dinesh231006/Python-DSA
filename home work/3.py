n,x=map(int,input().split())
arr=list(map(int,input().split()))
first=-1
second=-1
for i in range(n):
    if arr[i]==x:
        first=i
        break
for i in range(len(arr)):
    if arr[i]==x:
        second=i
print(first," ",second)