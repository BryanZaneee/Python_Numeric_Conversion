# Defines the main menu of the code
def main():
    while True:
        print("Decoding Menu")
        print("-------------")
        print("1. Decode hexadecimal")
        print("2. Decode binary")
        print("3. Convert binary to hexadecimal")
        print("4. Quit\n")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            hex = input("Please enter the numeric string to convert: ")
            res = hex_string_decode(hex)
            print(f"Result: {res}\n")
        elif choice == 2:
            binary = input("Please enter the numeric string to convert: ")
            res = binary_string_decode(binary)
            print(f"Result: {res}\n")
        elif choice == 3:
            binary = input("Please enter the binary string to convert: ")
            res = binary_to_hex(binary)
            print(f"Result: {res}\n")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Decodes letters within a hexadecimal value to their numerical value
def hex_char_decode(digit):
    if '0' <= digit <= '9':
        return ord(digit) - ord('0')
    elif 'a' <= digit <= 'f':
        return ord(digit) - ord('a') + 10
    elif 'A' <= digit <= 'F':
        return ord(digit) - ord('A') + 10
    else:
        return


# Converts a hexadecimal value to a decimal
def hex_string_decode(hex):
    res = 0
    if hex[:2] == '0x':
        hex = hex[2:]
        left_most_bit_index = len(hex) - 1
        for digit in hex:
            res += hex_char_decode(digit) * 16 ** left_most_bit_index
            left_most_bit_index -= 1
    return res


# Decodes a binary string to its numerical value
def binary_string_decode(binary):
    if binary[:2] == '0x':
        base = 16
        binary = binary[2:]
    elif binary[:2] == '0b':
        base = 2
        binary = binary[2:]
    else:
        base = 10

    res = 0
    left_most_bit_index = len(binary) - 1
    for digit in binary:
        res += int(digit, base) * (2 ** left_most_bit_index)
        left_most_bit_index -= 1

    return res

# Decodes a binary string, re-encodes it as a hexadecimal, and returns the hexadecimal
def binary_to_hex(binary):
    res = binary_string_decode(binary)
    hex_str = hex(res)[2:]
    return hex_str


# Enables to program to run
if __name__ == "__main__":
    main()
