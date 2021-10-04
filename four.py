#Input the number of test cases
t=int(input())
lst1=[]
lst2=[]
if(t>=1 and t<=10**5):
    for i in range(t):
      #Input the integer numbers for each test case
        n=int(input())
    #Store each number in a list for further operations
        if(n>=0 and n<=10**9):
            lst1.append(n)
    #Converting each number in the list to string in order to find its length
    for i in lst1:
        s=str(i)
        l=len(s)
        count=0
        k=0
    #For each number the number of occurences of 4 is calculated and stored in another list
        for j in range(l):
            while(i>0):
                k=i%10
                if(k==4):
                    count=count+1
                i=int(i/10)
        lst2.append(count)
    for i in lst2:
        print(i)
