i=1
while i<=4:
    k=1
    while k<=4:
        if  k==4 or i==1 or k==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
        k=k+1
    print()
    i=i+1
