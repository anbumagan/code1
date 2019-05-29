a=str(input())
if(len(a)<=1000):
   rev=a[::-1]
   if(a == rev):
      print("yes")
   else:
       print("no")
