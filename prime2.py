a,b=input().split()
n=int(a)
q=int(b)
c=0
for i in range(n+1,q):
    for j in range(2,i):
        if(i%j==0):
            break 
    else:
            print(i,"",end="")
