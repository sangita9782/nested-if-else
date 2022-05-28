i=1
while i<=5:
    j=1
    while j<=4:
        if i==1 or i==2 or i==4 or i==5 or j==1 or j==2 or j==3 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
        j=j+1
    print()
    i=i+1