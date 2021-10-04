#Input the number of test cases
T=int(input())
lst1=[]
lst2=[]
if(T>=1 and T<=1000):
    for i in range(T):
      #Input the number for each test case
        n=int(input())
        if(n>=1 and n<=10**6):
            lst1.append(n)
    for i in lst1:
        #temp=i
        sum=0
        s=str(i)
        l=len(s)
        last=i%10
        first=i/10**(l-1)
        sum=int(last+first)
        lst2.append(sum)
    for i in lst2:
        print(i)
