#Input the number of test cases
t=int(input())
l=[]
if(t>=1 and t<=100):
    for i in range(t):
      #Input the number for each test case
        n=int(input())
        if(n>=1 and n<=100):
            f=1
       #Calculate the factorial of each number and store them in a list
            for j in range(n):
                j=j+1
                f=f*j
            l.append(f)
      #Displaying the factorials of all given nunbers
    for i in l:
                print(i)
