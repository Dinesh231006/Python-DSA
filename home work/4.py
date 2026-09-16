n,c=map(int,input().split())
arr=list(map(int,input().split()))
a=0
for i in arr:
    if i>=c:
        a+=1
print(a)