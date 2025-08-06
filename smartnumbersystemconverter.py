def anytodecimal(num):
    # Ask the user for the base of the input number (e.g., 2 if the number is in binary)
    ibase = int(input("Enter input base:\n"))

    # If input is already in base 10, no need to convert — just go to output stage
    if ibase == 10:
        decimaltoany(num)
    else:
        # For other bases (like binary or octal), we convert to decimal first

        # Start from the highest digit (leftmost), so get its position (power of base)
        j = len(str(num)) - 1
        decimal = 0

        # Go through each digit and apply the formula: digit × base^position
        for i in str(num):
            decimal += (ibase ** j) * int(i)  # Add value of each digit according to its weight
            j -= 1  # Move to next lower power

        # Now the number is converted to base 10 — pass it to the next function
        decimaltoany(decimal)


def decimaltoany(decimal):
    # Ask the user for the base to which the number should be converted
    tbase = int(input("Enter target base:\n"))

    # If target base is 10, we don’t need to convert
    if tbase == 10:
        print(f"{decimal} is the requested number")
    else:
        # Start converting from decimal to the target base (like binary or octal)
        r = decimal  # just using a temporary variable

        arr = []  # this will store remainders (digits) in reverse order
        out = ""  # final output string

        # Divide the number by the target base repeatedly
        while r != 0:
            arr.append(r % tbase)  # store remainder (this is the current digit)
            r = int(r / tbase)     # update the number by integer division

        # Digits were collected from least significant to most significant
        # So we reverse them to get the correct order
        for i in arr:
            out += str(i)
        out = "".join(reversed(out))  # now the digits are in correct order

    # Print the final converted number
    print(f"{out} is the requested number!")


# Start by asking the user for the number they want to convert
num = int(input("Enter number:\n"))
anytodecimal(num)
