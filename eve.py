a,b=input().split()
n=int(a)
q=int(b)
for i in range(n+1,q):
    if(i%2==0):
        print(i,end=" ")
