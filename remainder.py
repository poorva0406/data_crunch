#Input the number of test cases
T=int(input())
lst=[]
if(T>=1 and T<=1000):
    for i in range(T):
      #Input the integers a and b so as to find the remainder of a/b
        a,b=map(int,input().split())
        if(a>=1 and a<=10000 and b>=1 and b<=10000):
            c=a%b
            lst.append(c)
    for i in lst:
        print(i)
