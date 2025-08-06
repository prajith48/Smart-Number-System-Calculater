def anytodecimal(num):
    ibase=int(input("Enter input base:\n"))
    if ibase == 10:
        decimaltoany(num)
    else:
        j=len(str(num))-1
        decimal=0
        for i in str(num):
            decimal+=(ibase**j)*int(i)
            j-=1
        decimaltoany(decimal)


def decimaltoany(decimal):
    tbase=int(input("Enter target base:\n"))
    if tbase==10:
        print(f"{decimal} is the requested number")
    else:
        r=decimal
        arr=[]
        out=""
        while r!=0:
            arr.append(r%tbase)
            r=int((r)/tbase)
        for i in arr:
            out+=str(i)
        out = "".join(reversed(out)) 
    print(f"{out} is the requested number!")


num=int(input("Enter number:\n"))
anytodecimal(num)
