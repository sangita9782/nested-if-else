i=1
while i<=5:
    c=1
    while c<=5-i:
        print(" ",end=" ")
        c=c+1
    k=1
    while k<=5:
        if  i==k or i==5 or k==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        k=k+1
    print()
    i=i+1