a,b=input().split()
n=int(a)
q=int(b)
for i in range(n+1,q):
    c=i
    sum=0
    while(i!=0):
        r=i%10
        sum=sum+r*r*r
        i=i//10
    if(c==sum):
        print(c,"",end=" ")
