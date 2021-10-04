#Input the number of testcases
T=int(input())
lst=[]
for i in range(T):
  #Input a and b i.e. the numbers to be added
    a,b=map(int,input().split())
    n=a+b
    lst.append(n)
for i in lst:
    print(i)
