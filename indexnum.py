n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
for i in range(0,n):
    if(a[i]==i):
        b.append(a[i])
if not b:
    b = ['-1'] 
sorted(b)
for j in b: 
    print(j, end=" ") 


    
