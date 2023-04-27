def decimal_to_hexadecimal(decimal):
    """
    Convert decimal number to hexadecimal representation.
    """
    if decimal == 0:
        return "0"
    hex_digits = "0123456789ABCDEF"
    if decimal < 0:
        sign = "-"
        decimal = abs(decimal)
    else:
        sign = ""
    hex_string = ""
    while decimal > 0:
        remainder = decimal % 16
        hex_string = hex_digits[remainder] + hex_string
        decimal //= 16
    return sign + hex_string


print(decimal_to_hexadecimal(10))