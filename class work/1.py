n=input()
arr=[]
for i in n:
    if i == " ":
        continue
    a=int(i)
    arr.append(a)
length=0
for i in arr:
    length=length+1
ab=0
for i in arr:
    if i == 0 :
        ab=ab+1
if ab!=0:
    print(f"{ab} student absent out of {length} student att : {int(((length-ab)/length)*100)}%")
else:
    print(f"no absent  att : {int(((length-ab)/length)*100)}%")