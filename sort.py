#Input the number of test cases
t=int(input())
if(t<=10**6):
    l1=[]
    for i in range(t):
      #Input the numbers to be sorted
        n=int(input())
        if(n>=0 and n<=10**6):
       #Storing those numbers in a list
            l1.append(n)
  #Sorting the list in ascending order
    l1.sort()
  #Displaying the sorted list of numbers
    for i in l1:
        print(i)
