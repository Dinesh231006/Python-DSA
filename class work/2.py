"""give n employee id's determine whether all id's are unique print yes if every id occurs ones otherwise print no.
input:1 5 9 17 3 6 
output:YES
input:2 3 9 2 5
output:NO"""

n=int(input(""))
for i in range(n):
    id=list(input("").split())
    a1=[]
    for i in id:
        if i not in a1:
            a1+=[i]
    if id==a1:
        print("YES")
    else:
        print("NO")