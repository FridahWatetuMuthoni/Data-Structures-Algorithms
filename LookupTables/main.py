# Creating a lookup table for squares of numbers 0-9
squares = [i * i for i in range(10)]

# Accessing precomputed square values
print(squares[2])  # Output: 4 (since 2^2 = 4)
print(squares[5])  # Output: 25 (since 5^2 = 25)



# Creating a lookup table for hexadecimal to binary conversion
hex_to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

# Accessing binary values using the lookup table
print(hex_to_bin['A'])  # Output: 1010
print(hex_to_bin['F'])  # Output: 1111
