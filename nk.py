a,b=input().split()
N=int(a)
K=int(b)
sum=0
L=input().split()
for i in range(0,K,1):
    sum=sum+int(L[i])
print(sum) 
