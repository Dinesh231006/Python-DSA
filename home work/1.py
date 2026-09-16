n=int(input())
arr=list(map(int,input().split()))
for i in range(n):
    print(arr[i],end=" ")
    if (i+1)%4==0:
        print("\n")
avg=sum(arr)/n
    
print(f"Average:{sum(arr)/n:.2f}")
print(f"Lowst score:{min(arr)}")
print(f"Highest score:{max(arr)}")
print("score  Deviation")
sd=0
for i in range(n):
    d=arr[i]-avg
    sd=sd+(d**2)
    print(arr[i]," ",d)
sd=(sd/n)**0.5
print(f"Standard deviation:{sd:.2f}")