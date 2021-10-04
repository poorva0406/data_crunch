n,k=map(int,input().split())
if(k<=10**7):
    count=0
    for i in range(n):
        t=int(input())
        if(t<=10**9):
            if(t%k==0):
                count+=1
    print(count)
