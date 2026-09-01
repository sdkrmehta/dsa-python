def addBinary(a: str, b: str):

    i = len(a) - 1
    j = len(b) - 1

    carry = 0
    result = ""

    while i >= 0 or j >= 0 or carry > 0:

        # Get digit from a
        if i >= 0:
            num1 = int(a[i])
        else:
            num1 = 0

        # Get digit from b
        if j >= 0:
            num2 = int(b[j])
        else:
            num2 = 0

        # Add both digits and carry
        total = num1 + num2 + carry

        # Find the binary digit
        if total == 0:
            digit = 0
            carry = 0

        elif total == 1:
            digit = 1
            carry = 0

        elif total == 2:
            digit = 0
            carry = 1

        else:                 # total == 3
            digit = 1
            carry = 1

        # Add digit to the beginning
        result = str(digit) + result

        i -= 1
        j -= 1

    return result


print(addBinary("11", "1"))