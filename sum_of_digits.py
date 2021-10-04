#Input the number of test cases
T=int(input())
if(T>=0 and T<=1000):
    lst1=[]
    lst2=[]
    for i in range(T):
    #Input the number for each testcase
        N=int(input())
        if(N>=0 and N<=10**6):
            lst1.append(N)
    for i in lst1:
        temp=i
        sum=0
    #Adding the digits of each number and storing it in a list
        while(i>0):
            a=i%10
            sum=sum+a
            i=int(i/10)
        lst2.append(sum)
    for i in lst2:
        print(i)
