def anytodecimal(num):
    ibase = int(input("Enter input base:\n"))
    
    # Convert num to string to handle decimal parts safely
    num_str = str(num)

    # Split integer and fractional part
    if '.' in num_str:
        intpart_str, frac_str = num_str.split('.')
    else:
        intpart_str = num_str
        frac_str = ''

    # Convert integer part to decimal
    decimal = 0
    j = len(intpart_str) - 1
    for i in intpart_str:
        decimal += (ibase ** j) * int(i)
        j -= 1

    # Convert fractional part to decimal
    k = -1
    for i in frac_str:
        decimal += (ibase ** k) * int(i)
        k -= 1

    decimaltoany(decimal)


def decimaltoany(decimal):
    tbase = int(input("Enter target base:\n"))
    
    if tbase == 10:
        print(f"{decimal} is the requested number")
    else:
        # Separate integer and fractional parts
        r = int(decimal)
        frac = decimal - r

        # Convert integer part using remainders
        arr = []
        if r == 0:
            arr.append('0')
        while r != 0:
            arr.append(str(r % tbase))
            r = int(r / tbase)
        intpart = "".join(reversed(arr))

        # Convert fractional part using multiplication
        fracpart = ''
        count = 0
        precision = int(input("Enter max digits after decimal: "))
        while frac != 0 and count < precision:
            frac *= tbase
            digit = int(frac)
            fracpart += str(digit)
            frac -= digit
            count += 1

        # Combine both parts
        if fracpart:
            out = f"{intpart}.{fracpart}"
        else:
            out = intpart

        print(f"{out} is the requested number!")


# Use input as float to accept decimal numbers
num = input("Enter number:\n")  # using string to avoid float error
anytodecimal(num)
