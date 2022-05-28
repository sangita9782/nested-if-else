i=1
while i<=4:
    j=1
    while j<=7:
        if i==4 or i+j==5 or j-i==3:
            print("*",end=" ") 
        else:
            print(" ",end=" ")
        j=j+1
    print()
    i=i+1
    