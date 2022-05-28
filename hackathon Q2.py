i=1
while i<=5:
    j=1
    while j<=5:
        if i==5 or j==1 or i+j==6:
            print("*",end=" ") 
        else:
            print(" ",end=" ")
        j=j+1
    print()
    i=i+1