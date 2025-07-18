import sys
import re
import math

# Ask for the temperature in either C, F, or K. Allow negatives and decimals. Case insensitive.
temp_a = input('Enter the temperature and degrees you want to convert from (e.g., -10 C or 14 F or 263.15 K): ').lower()

# search for c, f, or k in the input to detect the degrees entered
# if multiple degrees found then only use the first found
def first_degree(s):
    target_letters = {'c', 'f', 'k'}
    for index, char in enumerate(s):
        if char in target_letters:
            return char
    return None

degrees = first_degree(temp_a)

if degrees:
    # get the temp value
    match = re.match(r'(-?\d+(\.\d+)?)', temp_a)
    if match:
        temp_float = float(match.group(1))
    else:
        print('Invalid temperature input.')
        sys.exit()

    # calculate and output the temperature in the other temperatures
    match degrees:
        case 'c':
            f = math.ceil(((temp_float * 9/5) + 32) * 10) / 10
            k = math.ceil((temp_float + 273.15) * 10) / 10
            print(f'{temp_float} Celsius ({degrees.upper()}) is {f} Ferinheight (F) and {k} Kelvin (K)')
        case 'f':
            c = math.ceil(((temp_float - 32) * 5/9) * 10) / 10
            k = math.ceil(((temp_float -32) * 5/9 + 273.15) * 10) / 10
            print(f'{temp_float} Ferinheight ({degrees.upper()}) is {c} Celsius (C) and {k} Kelvin (K)')
        case 'k':
            c = math.ceil((temp_float - 273.15) * 10) / 10
            f = math.ceil(((temp_float - 273.15) * 9/5 +32) * 10) / 10
            print(f'{temp_float} Kelvin ({degrees.upper()}) is {c} Celsius (C) and {f} Ferinheight')
else:
    print('No degrees entered. Use C, F, or K.')