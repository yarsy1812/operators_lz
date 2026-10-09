n=int(input())
if n>=1 and n<=25:
    if n==1:print("N")
    elif n==2 or n==3 or n==5 or n==7 or n==11 or n==13 or n==17 or n==19 or n==23:
        print("Y")
    else:print("N")    
else:print("число не подходит")        